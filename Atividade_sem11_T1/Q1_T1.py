def deposito_juros(deposito,taxa):
  anos = 0
  juros = taxa/100
  deposito_total = deposito

  while deposito_total < deposito * 2:
        anos += 1
        deposito_total += deposito_total*juros

  return anos


def main():
    deposito = int(input())
    taxa = float(input())

    resultado = deposito_juros(deposito,taxa)

    print(resultado)

if __name__ == "__main__":
    main()
