def uniao(lista_um,lista_dois):
    lista_uniao = []

    for i in range(10):
        lista_uniao.append(lista_um[i])
    for i in range(10):
        lista_uniao.append(lista_dois[i])

    return lista_uniao

def verificacao(lista_uniao):
    lista_tres = []

    for i in range(20):
        if lista_uniao[i] not in lista_tres:
            lista_tres.append(lista_uniao[i])

    return lista_tres

def funcao():
    lista_um = []
    lista_dois = []

    for i in range(10):
        entrada = int(input())
        lista_um.append(entrada)

    for i in range(10):
        entrada = int(input())
        lista_dois.append(entrada)

    return lista_um, lista_dois

def main():
    lista_um, lista_dois = funcao()

    lista_uniao = uniao(lista_um,lista_dois)

    lista_tres = verificacao(lista_uniao)

    print(f"{lista_tres}")


if __name__ == "__main__":
    main()
