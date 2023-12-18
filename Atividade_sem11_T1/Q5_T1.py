def cartao_de_credito(salario, divida):
    mes = 10
    ano = 2016

    while divida <= salario:

        if mes == 3:
            salario *= 1.05
        divida *= 1.15
        mes += 1

        if mes > 12:
            mes = 1
            ano += 1

    return mes, ano


def main():
    salario = float(input())
    divida = float(input())

    mes, ano = cartao_de_credito(salario, divida)

    print(f"{mes}/{ano}")


if __name__ == "__main__":
    main()

