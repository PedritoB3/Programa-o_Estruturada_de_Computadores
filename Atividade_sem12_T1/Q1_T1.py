def corrida(metros_tartaruga):
    min = 0
    coelho = 0

    while True:
        if coelho < metros_tartaruga:
            min += 1

            coelho+=10

            metros_tartaruga+=1

        if coelho >= metros_tartaruga:
            return min

def main():
    metros_tartaruga = int(input())

    resultado = corrida(metros_tartaruga)

    print(f"{resultado}")




if __name__ == "__main__":
    main()
