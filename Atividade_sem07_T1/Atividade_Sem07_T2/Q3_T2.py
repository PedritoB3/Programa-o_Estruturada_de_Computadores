def reserva(num):
    if 10 <= num <= 99:
        dez = num // 10
        uni = num % 2 == 1

        contador = 0

        if uni:
            contador += 1
        if dez % 2 == 1:
            contador += 1

        if contador == 0:
            return "Nenhum dígito é ímpar."
        elif contador == 1:
            return "Apenas um dígito é ímpar."
        elif contador == 2:
            return "Os dois dígitos são ímpares."

def main():
    print("Escreva de 10 a 99 numero inteiro, e dirá quantos digitos ímpar tem:")
    num = int(input())
    resultado = reserva(num)

    print(f"{resultado}")
if __name__ == '__main__':
    main()
