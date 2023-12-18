def valor_media():
    valor_total = 0
    quantidade_numero = 0

    while True:
        num = int(input())

        if num == 0:
            break
        elif num > 0:
            valor_total += num
            quantidade_numero += 1

    media = valor_total/quantidade_numero

    return media


def main():

    resultado = valor_media()

    print(f"{resultado:.2f}")

if __name__ == "__main__":
    main()



