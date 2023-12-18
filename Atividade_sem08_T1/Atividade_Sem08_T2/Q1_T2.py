#01. Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja
#ímpar. Mostre na tela o resultado da operação.
def resposta(numero):
    if numero % 2 == 0:
        return int(numero+5)
    elif numero % 2 == 1:
        return int(numero+8)

def main():
    print("Escreva um número inteiro e somará com 5 caso valor lido seja par ou somará 8 caso o valor lido seja ímpar.")
    numero = int(input().strip())

    resultado = resposta(numero)

    print(f"O seu valor é {resultado}")

if __name__ == "__main__":
    main()

