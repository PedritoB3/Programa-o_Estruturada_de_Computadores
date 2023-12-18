def opcoes():
    while True:
        print("OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM")

        escolha = int(input())

        if escolha == 1:
            print("1 - Olá. Como vai?")

        elif escolha == 2:
            print("2 - Vamos estudar mais.")

        elif escolha == 3:
            print("3 - Meus Parabéns!")

        elif escolha == 0:
            print("0 - Fim de serviço.")
            break

        else:
            print("Opção inválida.")


def main():
    opcoes()

if __name__ == "__main__":
    main()
