#03. Escreva um programa que leia um número inteiro positivo e escreva na tela:

#• FIZZ se o número é divisível por três;
#• BUZZ se o número é divisível por cinco;
#• FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
#• O próprio número caso não seja divisível por três ou por cinco.
#OBS: para cada número lido apenas uma resposta deve ser impressa.

def operacao (n):
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    elif n % 3 == 0:
        return "FIZZ"
    elif n % 5 == 0:
        return "BUZZ"

    else:
        return n

def main():
    print("Digite um numero inteiro")
    print("FIZZ se o número é divisível por três;")
    print("BUZZ se o número é divisível por cinco;")
    print("FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.")
    numero = int(input().strip())
    resultado = operacao(numero)

    print(f'{resultado}')

if __name__ == "__main__":
    main()
