#Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os
#valores lidos:

#• Todos os valores são diferentes;
#• Existem dois valores iguais e um diferente;
#• Todos os valores são iguais.
def tres_numeros(num1,num2,num3):
    if num1!=num2==num3 or num1==num2!=num3 or num1==num3!=num2:
        return "Existem dois valores iguais e um diferente"
    if num1!=num2!=num3!=num1:
        return "Todos os valores são diferentes"
    elif int(num1==num2==num3):
        return "Todos os valores são iguais"


def main():
    print("Escreva três numeros aleatorios:")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    resultado = tres_numeros(n1,n2,n3)

    print(f"{resultado}")

if __name__ == "__main__":
    main()

