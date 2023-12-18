def horario(ho):
    horas = int(ho/60)
    minutos = int(ho%60)
    return horas, minutos

def main():
    print("Insira uma quantidade de minutos, ex:'220', que assim será convertido em horas e minutos")
    ho = int(input().strip())

    h, min = horario(ho)

    print(f"São {h}:{min}")

if __name__ == '__main__':
    main()
