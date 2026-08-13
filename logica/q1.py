def corrige_emails(emails):
    resultado = []
    
    for email in emails:
        tamanho = len(email)
        metade = tamanho // 2
        
        # Separa as duas metades considerando o piso da metade
        metade_esquerda = email[:metade]
        metade_direita = email[metade:]
        
        # Desfaz a inversao de dentro para fora
        esquerda_corrigida = metade_esquerda[::-1]
        direita_corrigida = metade_direita[::-1]
        
        # Junta as duas metades reconstruidas
        email_final = esquerda_corrigida + direita_corrigida
        
        # Valida se o dominio do email e exatamente @usp.br
        if email_final.endswith("@usp.br"):
            resultado.append(email_final)
        else:
            resultado.append("ERRO")
            
    return resultado


# --- BLOCO DE TESTES LOCAIS ---
if __name__ == "__main__":
    # Teste 1 (Exemplo do Enunciado)
    entrada_1 = [
        "id_atanerrb.psu@av",
        "t.alalalimacrb.repsu@ppo",
        ".orbmem_ovonrb.psu@gnirut"
    ]
    print("Teste 1:", corrige_emails(entrada_1))
    # Saida esperada: ['renata_diva@usp.br', 'ERRO', 'novo_membro.turing@usp.br']

    # Teste 2 (Exemplo do Apendice)
    entrada_2 = [
        "sac_tsetrb.psu@1e",
        "c_tsetortuorb.psu@1esa",
        "c_tsetortuorb.5psu@1esa",
        ".ed.olpmexerb.psu@liame",
        "_odnatsetrb.psu@b1q",
        "tset_omitlurb.psu@esac"
    ]
    print("Teste 2:", corrige_emails(entrada_2))
    # Saida esperada: ['test_case1@usp.br', 'outrotest_case1@usp.br', 'ERRO', 'exemplo.de.email@usp.br', 'testando_q1b@usp.br', 'ultimo_testcase@usp.br']