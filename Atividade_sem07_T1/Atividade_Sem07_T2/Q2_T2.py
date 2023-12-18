def reserva(num):
    if 100 <= num <= 999:
        cen = num // 100
        dez = (num % 100) // 10
        uni = num % 10

        contador = 0

        if cen % 2 == 0:
            contador += 1
        if dez % 2 == 0:
            contador += 1
        if uni % 2 == 0:
            contador += 1

        if contador == 0:
            return 0
        elif contador == 1:
            return 1
        elif contador == 2:
            return 2
        elif contador == 3:
            return 3
        else:
            return 0

def main():
    print("Digite um numero inteiro entre 100 a 999, e dirá quantos digitos pares  existe neste numero:")
    num = int(input())
    resultado = reserva(num)

    print(f"Tem {resultado} digito par")
if __name__ == '__main__':
    main()
