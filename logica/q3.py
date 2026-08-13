def organiza_listas(qtd_projetos, episodios, min_passos):
    # Dicionario para armazenar a lista de episodios de cada projeto (chaves de 1 ate qtd_projetos)
    projetos_map = {i: [] for i in range(1, qtd_projetos + 1)}
    # Dicionario para acompanhar o ultimo indice visto de cada projeto
    ultimo_indice = {i: -1 for i in range(1, qtd_projetos + 1)}

    for ep in episodios:
        proj_id, indice, passos = ep
        
        # Validacao de Ordem Cronologica:
        # Se o indice atual for menor ou igual ao ultimo registrado para este projeto, houve erro grave.
        if ultimo_indice[proj_id] != -1 and indice <= ultimo_indice[proj_id]:
            # Descarta tudo de todos os projetos
            listas_vazias = [[] for _ in range(qtd_projetos)]
            return "nao", listas_vazias
            
        ultimo_indice[proj_id] = indice
        projetos_map[proj_id].append(ep)

    # Lista final com os resultados ordenados do projeto 1 ate qtd_projetos
    resultado_listas = []
    pelo_menos_um_valido = False

    for proj_id in range(1, qtd_projetos + 1):
        eps_projeto = projetos_map[proj_id]
        soma_passos = sum(ep[2] for ep in eps_projeto)
        
        # Se a duracao total de passos nao atingir o minimo, descarta apenas os dados deste projeto
        if soma_passos >= min_passos and len(eps_projeto) > 0:
            resultado_listas.append(eps_projeto)
            pelo_menos_um_valido = True
        else:
            resultado_listas.append([])

    status = "sim" if pelo_menos_um_valido else "nao"
    return status, resultado_listas


# --- BLOCO DE TESTES LOCAIS ---
if __name__ == "__main__":
    # Teste 1 (Exemplo 1 do Enunciado) -> Deve retornar 'sim'
    episodes_ex1 = [
        [2, 128, 30], [3, 10, 100], [1, 13, 200], [1, 78, 80],
        [2, 256, 70], [1, 130, 120], [5, 1, 40], [2, 512, 50],
        [3, 100, 150], [5, 680, 200], [5, 681, 60], [1, 198, 300]
    ]
    status1, listas1 = organiza_listas(5, episodes_ex1, 250)
    print("Teste 1 Status:", status1)
    print("Teste 1 Listas:", listas1)

    # Teste 2 (Exemplo 2 do Enunciado - Erro no Projeto 2: indice 92 depois 3) -> Deve retornar 'nao'
    episodes_ex2 = [
        [1, 25, 50], [1, 48, 160], [2, 92, 100], [3, 1, 400],
        [2, 3, 400], [1, 64, 90], [2, 123, 700], [4, 343, 30],
        [5, 70, 20], [5, 71, 30], [3, 200, 700], [5, 400, 10],
        [6, 55, 80], [1, 99, 50]
    ]
    status2, listas2 = organiza_listas(6, episodes_ex2, 300)
    print("\nTeste 2 Status:", status2)
    print("Teste 2 Listas:", listas2)