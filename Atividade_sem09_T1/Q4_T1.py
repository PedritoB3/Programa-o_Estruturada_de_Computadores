#Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui
#menor diferença com relação ao primeiro, imprimindo o valor da diferença.

def valores(num1,num2,num3):
    valor2 = abs(num1-num2)
    valor3 = abs(num1-num3)
    if valor2 < valor3:
        return valor2
    else:
        return valor3

def main():
    print("Digite três valores aleatórios")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    resultado = valores(num1,num2,num3)

    print(f"O valor com a menor diferença em relação ao primeiro, atraves do valor da diferença é: {resultado}")

if __name__ == "__main__":
    main()


