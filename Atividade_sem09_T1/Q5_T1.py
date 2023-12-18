#Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco).
#A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:

#• Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
#• Se 1 (um), escreva se o valor lido é par ou ímpar;
#• Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
#• Se 3 (três), escreva a divisão inteira do valor lido por 10;
#• Se 4 (quatro), escreva o quadrado do valor lido;

def zero(n):
    return 9*n+7

def um(n):
    if n%2 == 0:
        return "par"
    elif n%2 == 1:
        return "ímpar"

def dois(n):
    return 5*(n**2)-(3*n)+42

def tres(n):
    return n//10

def quatro(n):
    return n*n

def operacao(num):
    resto = num%5

    if resto == 0:
        return zero(num)
    elif resto == 1:
        return um(num)
    elif resto == 2:
        return dois(num)
    elif resto == 3:
        return tres(num)
    elif resto == 4:
        return quatro(num)


def main():
    print("Digite um numero aleatorio:")
    num = int(input())
    print("de acordo com o resultado da divisão,")
    print("Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;")
    print("Se 1 (um), escreva se o valor lido é par ou ímpar;")
    print("Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;")
    print("Se 3 (três), escreva a divisão inteira do valor lido por 10;")
    print("Se 4 (quatro), escreva o quadrado do valor lido;")

    resposta = operacao(num)

    print(f"\nO resultado da operação foi: {resposta}")

if __name__ == "__main__":
    main()
