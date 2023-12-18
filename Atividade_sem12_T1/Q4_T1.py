def num_sorte(data_nas):
    num_sorte = 0
    while data_nas > 0:
        ultimo_digito = data_nas % 10

        num_sorte += ultimo_digito

        data_nas //= 10

    return num_sorte

def main():
    numero = int(input())

    resultado = num_sorte(numero)

    print(f"{resultado}")

if __name__ == "__main__":
    main()
