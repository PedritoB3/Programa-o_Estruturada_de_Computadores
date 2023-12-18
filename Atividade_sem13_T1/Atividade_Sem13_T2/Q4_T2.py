#4. Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de
#um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos
#anteriores da lista original.
#IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna
#uma lista com a soma cumulativa. Por exemplo:

def soma_cumulativa(minha_lista,contagem):
    minha_lista_soma = []
    soma = 0

    for i in range(contagem):
        soma += minha_lista[i]

        minha_lista_soma.append(soma)

    return minha_lista_soma

def main():
    minha_lista = []
    contagem = 0
    while True:
        usuario_entrada = int(input("Digite uma quantidade indeterminada de numeros. Digite 0 para terminar: "))

        if usuario_entrada == 0:
            break
        else:
            minha_lista.append(usuario_entrada)
            contagem +=1

    minha_lista_soma = soma_cumulativa(minha_lista,contagem)

    print(f"Esta é a soma dos elementos anteriores a lista original: {minha_lista_soma}")

if __name__ == '__main__':
    main()
