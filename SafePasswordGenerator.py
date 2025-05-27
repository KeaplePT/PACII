import secrets
import string

def gerar(tam=12):
    base = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    return ''.join(secrets.choice(base) for _ in range(tam))

if __name__ == "__main__":
    print(gerar())
