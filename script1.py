def verif(p):
    if len(p) < 8:
        return "Erro: mínimo 8 caracteres."
    if not any(c.isupper() for c in p):
        return "Erro: falta maiúscula."
    if not any(c.islower() for c in p):
        return "Erro: falta minúscula."
    if not any(c.isdigit() for c in p):
        return "Erro: falta número."
    if not any(c in "!@#$%^&*()-_+=" for c in p):
        return "Erro: falta símbolo especial."
    return "Password válida"

if __name__ == "__main__":
    entrada = input("Password: ")
    print(verif(entrada))
