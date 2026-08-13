import pandas as pd
import numpy as np

# 1. Carregamento do Dataset
url_dataset = "https://drive.google.com/uc?id=1_dPruQi9XN6JIbZ8sAwpGQDX6MZyIgeI"
df = pd.read_csv(url_dataset)

print("--- Formato do Dataset ---")
print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}\n")

print("--- Visão Geral dos Tipos e Nulos ---")
print(df.info())

print("\n--- Estatísticas Descritivas Iniciais ---")
display(df.describe())