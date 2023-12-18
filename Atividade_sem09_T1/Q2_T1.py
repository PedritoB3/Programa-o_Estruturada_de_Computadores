#Escreva um programa que leia dois valores e uma das seguintes operações a serem executadas (codificadas da
#seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa
#operação sobre os dois valores lidos.
def operacao(num1,num2,resposta):
     if resposta == 1:
         return float(num1+num2)
     elif resposta == 2:
         return float(num1-num2)
     elif resposta == 3:
         return float(num1*num2)
     elif resposta == 4:
         return float(num1/num2)

def main():
    print("Digite dois valores aleatorios")
    num1 = int(input())
    num2 = int(input())
    print("Qual operação você deseja realizar?. Ex:1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão.")
    resposta = int(input())

    resultado = operacao(num1,num2,resposta)

    print(f"O resultado é{resultado:.2f}")

if __name__ == "__main__":
    main()

