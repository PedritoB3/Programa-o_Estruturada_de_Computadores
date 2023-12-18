def valor_maior_menor():
    num = int(input())
    num_maior = num
    num_menor = num

    while True:
        num = int(input())

        if num == 0:
            break
        if num > num_maior:
            num_maior = num

        if num < num_menor:
            num_menor = num


    return num_maior,num_menor


def main():

    maior,menor = valor_maior_menor()

    print(f"{maior}\n{menor}")

if __name__ == "__main__":
    main()


