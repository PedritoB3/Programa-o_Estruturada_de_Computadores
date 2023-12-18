def lista_verificacao(lista):
    lista_par = []
    lista_impar = []
    for i in range(20):
        if lista[i] % 2 == 0:
            lista_par.append(lista[i])

        elif lista[i] % 2 == 1:
            lista_impar.append(lista[i])

def main():
    lista = []
    lista_par = []
    lista_impar = []

    for i in range(20):
        usuario_entrada = int(input())
        lista.append(usuario_entrada)

        if usuario_entrada % 2 == 0:
            lista_par.append(usuario_entrada)

        elif usuario_entrada % 2 == 1:
            lista_impar.append(usuario_entrada)

    print(f"{lista}\n{lista_par}\n{lista_impar}")


if __name__ == '__main__':
    main()
