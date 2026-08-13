# Criando uma cópia para o processo de limpeza
df_clean = df.copy()

# 1. Remoção de duplicatas exatas e exclusão de IDs irrelevantes para os modelos
df_clean = df_clean.drop_duplicates()
if 'student_id' in df_clean.columns:
    df_clean = df_clean.drop(columns=['student_id'])

# 2. Tratamento de Inconsistências Conhecidas (Regras de Domínio)
# a) Horas de estudo e sono não podem ser negativas
if 'study_time_hours' in df_clean.columns:
    df_clean.loc[df_clean['study_time_hours'] < 0, 'study_time_hours'] = np.nan

if 'sleep_hours' in df_clean.columns:
    df_clean.loc[df_clean['sleep_hours'] < 0, 'sleep_hours'] = np.nan

# b) Porcentagem de presença deve estar estritamente entre 0 e 100
if 'attendance_percent' in df_clean.columns:
    df_clean.loc[(df_clean['attendance_percent'] < 0) | (df_clean['attendance_percent'] > 100), 'attendance_percent'] = np.nan

# c) Notas anteriores e nota final devem estar dentro de limites plausíveis (ex: 0 a 100)
for col_nota in ['previous_grade', 'final_exam_score']:
    if col_nota in df_clean.columns:
        df_clean.loc[(df_clean[col_nota] < 0) | (df_clean[col_nota] > 100), col_nota] = np.nan

# 3. Tratamento de Valores Ausentes (Imputação Estratégica)
# Preenchimento de colunas numéricas com a mediana (mais robusta a outliers)
colunas_numericas = df_clean.select_dtypes(include=[np.number]).columns
for col in colunas_numericas:
    if df_clean[col].isna().sum() > 0:
        mediana = df_clean[col].median()
        df_clean[col] = df_clean[col].fillna(mediana)

# Preenchimento de colunas categóricas com a moda (valor mais frequente)
colunas_categoricas = df_clean.select_dtypes(include=['object', 'category']).columns
for col in colunas_categoricas:
    if df_clean[col].isna().sum() > 0:
        moda = df_clean[col].mode()[0]
        df_clean[col] = df_clean[col].fillna(moda)

# 4. Verificação Final da Limpeza
print("--- Resumo de Nulos Pós-Limpeza ---")
print(df_clean.isna().sum())
print(f"\nDimensão final do dataset limpo: {df_clean.shape}")