#Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores
#são diferentes. NÃO use as funções embutidas min() e max().

def numeros(num1,num2,num3,num4,num5):
    num = [num1,num2,num3,num4,num5]
    num.sort(key=int)
    maior = num[4]
    menor = num[0]
    return maior, menor

def main():
    num1 = int(input("Digite o valor 1:").strip())
    num2 = int(input("Digite o valor 2:").strip())
    num3 = int(input("Digite o valor 3:").strip())
    num4 = int(input("Digite o valor 4:").strip())
    num5 = int(input("Digite o valor 5:").strip())

    num_maior, num_menor = numeros(num1,num2,num3,num4,num5)
    print(f"Esse valor é o maior: {num_maior}\nE esse é o menor: {num_menor}")

if __name__ == "__main__":
    main()
