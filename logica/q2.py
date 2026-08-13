def estacionamento_ok(K, instantes):
    stack = []
    
    for c in instantes:
        if c > 0:
            if len(stack) >= K:
                return "nao"
            stack.append(c)
        else:
            carro_saindo = abs(c)
            if not stack or stack[-1] != carro_saindo:
                return "nao"
            stack.pop()
            
    if len(stack) != 0:
        return "nao"
        
    return "sim"


# --- BLOCO DE TESTES LOCAIS ---
if __name__ == "__main__":
    print("Teste 1:", estacionamento_ok(3, [1, 2, -2, 3, -3, -1]))
    
    print("Teste 2:", estacionamento_ok(3, [1, 2, -2, 3, 5, -3, -1, -5]))
    
    print("Teste 3:", estacionamento_ok(2, [-1, 1, 2, -2]))
    
    print("Teste 4:", estacionamento_ok(5, [1, 2, 3, 4, -4, 5, 6, -6, -5, -3, -2, -1]))
    
    print("Teste 5:", estacionamento_ok(4, [1, 2, -1, -2, 3, 4, -3, -4]))