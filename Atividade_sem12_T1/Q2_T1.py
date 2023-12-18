def preco_carro(valor):
    poupanca = 10000
    rendimento = 0.7/100
    taxa = 0.4/100
    meses = 0

    while True:
        if poupanca < valor:
            meses += 1

            poupanca += poupanca * rendimento

            valor += valor * taxa

        if poupanca >= valor:
            return meses

def main():
    valor_carro = float(input())

    resultado = preco_carro(valor_carro)

    print(f"{resultado}")

if __name__ == "__main__":
    main()


