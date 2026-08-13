def organiza_listas(qt_p, eps, min_steps):
    p_map = {i: [] for i in range(1, qt_p + 1)}
    last_one = {i: -1 for i in range(1, qt_p + 1)}

    for ep in eps:
        proj_id, i, steps = ep
        
        if last_one[proj_id] != -1 and i <= last_one[proj_id]:
            listas_vazias = [[] for _ in range(qt_p)]
            return "nao", listas_vazias
            
        last_one[proj_id] = i
        p_map[proj_id].append(ep)

    resultado_listas = []
    pelo_menos_um_valido = False

    for proj_id in range(1, qt_p + 1):
        eps_projeto = p_map[proj_id]
        soma_passos = sum(ep[2] for ep in eps_projeto)
        
        if soma_passos >= min_steps and len(eps_projeto) > 0:
            resultado_listas.append(eps_projeto)
            pelo_menos_um_valido = True
        else:
            resultado_listas.append([])

    status = "sim" if pelo_menos_um_valido else "nao"
    return status, resultado_listas


# --- LOCAL TESTS ---
if __name__ == "__main__":
    
    episodes_ex1 = [
        [2, 128, 30], [3, 10, 100], [1, 13, 200], [1, 78, 80],
        [2, 256, 70], [1, 130, 120], [5, 1, 40], [2, 512, 50],
        [3, 100, 150], [5, 680, 200], [5, 681, 60], [1, 198, 300]
    ]
    status1, listas1 = organiza_listas(5, episodes_ex1, 250)
    print("Teste 1 Status:", status1)
    print("Teste 1 Listas:", listas1)

    episodes_ex2 = [
        [1, 25, 50], [1, 48, 160], [2, 92, 100], [3, 1, 400],
        [2, 3, 400], [1, 64, 90], [2, 123, 700], [4, 343, 30],
        [5, 70, 20], [5, 71, 30], [3, 200, 700], [5, 400, 10],
        [6, 55, 80], [1, 99, 50]
    ]
    status2, listas2 = organiza_listas(6, episodes_ex2, 300)
    print("\nTeste 2 Status:", status2)
    print("Teste 2 Listas:", listas2)