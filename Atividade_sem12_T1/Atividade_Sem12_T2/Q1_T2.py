def fatorial(numero):
    valor = 1

    while numero >= 0:
        if numero > 0:
            valor *= numero
            numero -= 1

        if numero == 0:
            return valor
def main():
    numero = int(input())
    valor = fatorial(numero)

    print(f"{valor}")
if __name__ == "__main__":
    main()
