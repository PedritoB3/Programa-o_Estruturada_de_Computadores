def verificacao(lista):
    lista_nova = []
    for i in lista:
        if i not in lista_nova :
            lista_nova.append(i)

    return lista_nova

def lista_funcao():
    lista = []

    for i in range(20):
        entrada = int(input())

        lista.append(entrada)

    return lista

def main():
    lista = lista_funcao()

    lista_nova = verificacao(lista)

    print(f"{lista_nova}")

if __name__ == "__main__":
    main()
