def fix_emails(emails):
    res = []
    
    for email in emails:
        t = len(email)
        half = t // 2
        
        left_side = email[:half]
        right_side = email[half:]
        
        left_fix = left_side[::-1]
        right_fix = right_side[::-1]
        
        email_final = left_fix + right_fix
        
        if email_final.endswith("@usp.br"):
            res.append(email_final)
        else:
            res.append("ERRO")
            
    return res


# --- LOCAL TESTS ---
if __name__ == "__main__":
    entrada_1 = [
        "id_atanerrb.psu@av",
        "t.alalalimacrb.repsu@ppo",
        ".orbmem_ovonrb.psu@gnirut"
    ]
    print("Teste 1:", fix_emails(entrada_1))

    entrada_2 = [
        "sac_tsetrb.psu@1e",
        "c_tsetortuorb.psu@1esa",
        "c_tsetortuorb.5psu@1esa",
        ".ed.olpmexerb.psu@liame",
        "_odnatsetrb.psu@b1q",
        "tset_omitlurb.psu@esac"
    ]
    print("Teste 2:", fix_emails(entrada_2))