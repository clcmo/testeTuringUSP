def estacionamento_ok(K, instantes):
    pilha = []
    
    for c in instantes:
        if c > 0:
            # Tenta estacionar: verifica se atingiu a capacidade maxima K
            if len(pilha) >= K:
                return "nao"
            pilha.append(c)
        else:
            # Tenta sair: precisa ser exatamente o topo da pilha
            carro_saindo = abs(c)
            if not pilha or pilha[-1] != carro_saindo:
                return "nao"
            pilha.pop()
            
    # Todos os carros precisam ter saido ao final
    if len(pilha) != 0:
        return "nao"
        
    return "sim"


# --- BLOCO DE TESTES LOCAIS ---
if __name__ == "__main__":
    # Teste 1 (Exemplo 1 do Enunciado) -> Deve retornar 'sim'
    print("Teste 1:", estacionamento_ok(3, [1, 2, -2, 3, -3, -1]))
    
    # Teste 2 (Exemplo 2 do Enunciado) -> Deve retornar 'nao'
    print("Teste 2:", estacionamento_ok(3, [1, 2, -2, 3, 5, -3, -1, -5]))
    
    # Teste 3 (Apêndice - Início inválido) -> Deve retornar 'nao'
    print("Teste 3:", estacionamento_ok(2, [-1, 1, 2, -2]))
    
    # Teste 4 (Apêndice - Fluxo longo válido) -> Deve retornar 'sim'
    print("Teste 4:", estacionamento_ok(5, [1, 2, 3, 4, -4, 5, 6, -6, -5, -3, -2, -1]))
    
    # Teste 5 (Apêndice - Ordem errada de saída) -> Deve retornar 'nao'
    print("Teste 5:", estacionamento_ok(4, [1, 2, -1, -2, 3, 4, -3, -4]))