def soma_numero():
    soma = 0

    while True:
        num = int(input())

        if num > 0:
            soma+=num
            continue
        elif num == 0:
            return soma

def main():
    resultado = soma_numero()

    print(f"{resultado}")

if __name__ == "__main__":
    main()
