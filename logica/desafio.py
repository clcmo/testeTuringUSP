def contar_caminhos_lacuna(inicio, fim, max_prof, transicoes, qtd_estados):
    """
    Funcao auxiliar de Backtracking (DFS) para contar quantos caminhos validos
    existem de 'inicio' ate 'fim' utilizando entre 1 e 'max_prof' passos intermediarios.
    """
    total_caminhos = 0
    
    def dfs(no_atual, prof_atual):
        nonlocal total_caminhos
        if prof_atual > max_prof:
            return
        
        for proximo in range(1, qtd_estados + 1):
            if transicoes.get((no_atual, proximo), 0) == 1:
                # Se a transicao do ultimo passo intermediario para 'fim' for valida,
                # encontramos 1 caminho valido!
                if transicoes.get((proximo, fim), 0) == 1:
                    total_caminhos += 1
                
                # Continua a exploracao para caminhos mais profundos
                if prof_atual < max_prof:
                    dfs(proximo, prof_atual + 1)

    dfs(inicio, 1)
    return total_caminhos


def conta_correcoes(qtd_estados, transicoes, episodio, max_prof):
    houve_lacuna = False
    total_correcoes = 1

    # Verifica cada transicao consecutiva no episodio
    for i in range(len(episodio) - 1):
        estado_origem = episodio[i]
        estado_destino = episodio[i + 1]

        # Checa se e uma transicao proibida (lacuna)
        if transicoes.get((estado_origem, estado_destino), 0) == 0:
            houve_lacuna = True
            caminhos = contar_caminhos_lacuna(
                estado_origem, estado_destino, max_prof, transicoes, qtd_estados
            )

            # Se uma lacuna nao tem solucao, o episodio inteiro nao pode ser corrigido
            if caminhos == 0:
                return 0

            total_correcoes *= caminhos

    # Se nao havia nenhuma lacuna no episodio, retorna -1
    if not houve_lacuna:
        return -1

    return total_correcoes


# --- BLOCO DE TESTES LOCAIS ---
if __name__ == "__main__":
    t_ex1 = {
        (1, 1): 1, (1, 2): 1, (1, 3): 0,
        (2, 1): 1, (2, 2): 0, (2, 3): 1,
        (3, 1): 1, (3, 2): 0, (3, 3): 0
    }

    # Teste 1 (Exemplo 1 do Enunciado) -> Deve retornar 8
    print("Teste 1:", conta_correcoes(3, t_ex1, [1, 2, 3, 3, 2], 3))

    # Teste 2 (Exemplo 2 do Enunciado - Sem lacunas) -> Deve retornar -1
    print("Teste 2:", conta_correcoes(3, t_ex1, [1, 2, 3, 1, 2], 1))

    # Teste 3 (Apêndice - Produto de lacunas) -> Deve retornar 32
    print("Teste 3:", conta_correcoes(3, t_ex1, [1, 2, 3, 2, 1, 3, 3, 1], 3))