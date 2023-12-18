def invertido(num):
    numero_invertido = 0

    while num > 0:
        numeracao = num % 10

        numero_invertido = numero_invertido * 10 + numeracao

        num //= 10

    return numero_invertido

def main():
    numero = int(input())

    numero_invertido = invertido(numero)

    print(numero_invertido)

if __name__ == "__main__":
    main()

