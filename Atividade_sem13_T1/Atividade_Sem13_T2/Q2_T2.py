#2. Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a
#ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são
#multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
#DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.

def ordem_multiplicacao(lista):
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i]*=3
        else:
            lista[i]*=5


def main():
    lista = []

    for i in range(100):
        usuario_entrada = int(input(f"Digite de {i+1}/100 numeros: "))

        lista.append(usuario_entrada)

    lista_ordenada = sorted(lista)

    ordem_multiplicacao(lista_ordenada)


    print(f"Esta é a lista ordenada e multiplicada entre par e impar: {lista_ordenada}")

if __name__ == '__main__':
    main()
