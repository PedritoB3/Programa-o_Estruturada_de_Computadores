#03.Escreva um programa que gere a seguinte sequência: 10, 20, 30, 40, ..., 990, 1000. Considere a separação dos números por vírgula seguido de espaço em brando e o pontos no final da sequência.

def valor_medio(numero):
    num = 0
    for i in range(1,101):
        numero = int(input())
        num+=numero
    resultado = num/100
    print(f"Esse é o valor medio dos mesmos: {resultado:.2f}")

def main():
    numero = 0
    print("Digite 100 numeros diferentes:")
    resultado = valor_medio(numero)

if __name__ == '__main__':
    main()
