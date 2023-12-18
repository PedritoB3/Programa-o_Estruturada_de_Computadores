def verificacao(lista):
    num_negativo = 0
    soma_positivos = 0

    for i in range(10):
        if lista[i] > 0:
            soma_positivos += lista[i]
        elif lista[i] < 0:
            num_negativo += 1

    return soma_positivos, num_negativo

def lista_funcao_real():
    lista = []

    for i in range(10):
        entrada = int(input())

        lista.append(entrada)

    return lista

def main():
    lista = lista_funcao_real()

    soma, num_negativo = verificacao(lista)

    print(f"{lista}\n{num_negativo}\n{soma}")


if __name__ == "__main__":
    main()
