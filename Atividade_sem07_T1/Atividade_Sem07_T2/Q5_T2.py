def numeros(num1,num2, num3):
    menor = min(num1,num2,num3)
    maior = max(num1,num2,num3)
    meio = num1+num2+num3-menor-maior
    return menor,meio,maior

def main():
    print("Digite três numeros diferentes:")
    print("Numero 1:")
    num1 = int(input())
    print("Numero 2:")
    num2 = int(input())
    print("Numero 3:")
    num3 = int(input())

    a,b,c = numeros(num1,num2,num3)

    print(f"A ordem crescente é: \n{a}\n{b}\n{c}")
if __name__ == '__main__':
    main()

