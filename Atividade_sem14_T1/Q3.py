#3. Leia duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo
#tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.
#Exemplo:

#0 1 2 18 19
#A = 23 37 30 . . . 45 35
#B = 30 32 46 . . . 33 42
#C = 53 69 76 . . . 88 77

def lista_AB(lista_A,lista_B):
    lista_C = []
    for i in range(20):
        soma = lista_A[i]+lista_B[i]
        lista_C.append(soma)
    return lista_C

def main():
    lista_A = []
    lista_B = []
    for i in range(20):
        entrada_A = int(input(f"Digite 20 numeros aleatorios da lista A,{i+1} numero digitado: "))
        lista_A.append(entrada_A)

    for i in range(20):
        entrada_B = int(input(f"Digite 20 numeros aleatorios da lista B,{i+1} numero digitado: "))
        lista_B.append(entrada_B)

    lista_C = lista_AB(lista_A, lista_B)

    print(f"Esta é a lista A: {lista_A}\nEsta é a lista B{lista_B}\nEsta é a soma dos elementos A e B:{lista_C}")

if __name__ == "__main__":
    main()
