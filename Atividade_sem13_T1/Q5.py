def lista_AB(lista_A,lista_B):
    lista_C = []
    for i in range(25):
        lista_C.append(lista_A[i])
        lista_C.append(lista_B[i])
    return lista_C

def main():
    lista_A = []
    lista_B = []
    for i in range(25):
        entrada_A = int(input())
        lista_A.append(entrada_A)

    for i in range(25):
        entrada_B = int(input())
        lista_B.append(entrada_B)

    lista_C = lista_AB(lista_A, lista_B)

    print(f"{lista_A}\n{lista_B}\n{lista_C}")

if __name__ == "__main__":
    main()
