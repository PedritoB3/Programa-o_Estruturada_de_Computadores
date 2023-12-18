def caractere(ca):
       if ca in "AEIOUaeiou":
        return "vogal"
       elif ca in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        return "consoante"
       elif ca in "01234567891011121314151617181920":
        return "número"
       elif  ca in "!@#$%¨&*()_-=+{}?:;<>çÇÁÉÍÓÚáéíóúÃÕÂÊÎÔÛ´~^/ ":
        return "símbolo"

def main():
    print("Insira um caractere e mostrara uma das mensagens: vogal, consoante, número ou símbolo:")
    resposta = input().strip()
    resultado = caractere(resposta)

    print(resultado)
if __name__ == '__main__':
    main()

