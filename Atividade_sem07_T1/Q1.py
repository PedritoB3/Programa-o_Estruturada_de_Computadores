def nome_precedido(np,nome):
    if np == 1:
        return f"Ilmo Sr. {nome}"
    elif np == 2:
        return f"Ilma Sra. {nome}"

def main():
    print("Insira seu nome:")
    nome = input()
    print("Insira seu sexo em numero inteiro, sendo 1=masculino, e 2=feminino:")
    np = int(input())
    resultado = nome_precedido(np, nome)
    print(f"Seu nome é {resultado}")
if __name__ == '__main__':
    main()
