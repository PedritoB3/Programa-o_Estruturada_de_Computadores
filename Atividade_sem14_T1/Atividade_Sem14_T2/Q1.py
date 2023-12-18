def maior_elemento(lista):
    maior_lista = lista[0]

    posicao = 0

    for i in range(10):
        if maior_lista < lista[i]:
            maior_lista = lista[i]
            posicao = i
    return maior_lista, posicao

def lista_funcao():
    lista = []

    for i in range(10):
        entrada = int(input())

        lista.append(entrada)

    return lista

def main():
    lista = lista_funcao()

    maior_lista, posicao = maior_elemento(lista)

    print(f"{lista}\n{maior_lista}\n{posicao}")

if __name__ == "__main__":
    main()
