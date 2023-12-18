def calculo(n):
    H = 0
    denominador = 0
    contador = 0
    while n >= 0:
        denominador +=1
        H += 1 / denominador

        contador += 1

        if contador == n:
            return f"{H:.4f}"

def main():
    numero = int(input())

    resultado = calculo(numero)

    print(f"{resultado}")


if __name__ == "__main__":
    main()




