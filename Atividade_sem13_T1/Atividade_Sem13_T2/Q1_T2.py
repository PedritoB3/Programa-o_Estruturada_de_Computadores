#1. Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura
#de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista
#onde cada valor da lista original é a multiplicado pelo valor da constante.
#IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e
#o valor da constante e retorna uma nova lista com os elementos multiplicados.

def multiplica_constante(lista, contagem,numero_constante):
    lista_multiplicada = []
    for i in range(contagem):
        multiplicacao = lista[i]*numero_constante

        lista_multiplicada.append(multiplicacao)

    return lista_multiplicada


def main():
    lista = []
    contagem = 0
    while True:
        usuario_entrada = int(input("Escreva quantidade de numeros inderteminadas. Digite 0 para finalizar: "))

        if usuario_entrada == 0:
            break
        else:
            lista.append(usuario_entrada)
            contagem += 1

    numero_constante = int(input("Agora digite o numero que irá multiplicar: "))

    resultado = multiplica_constante(lista,contagem,numero_constante)

    print(f"Esta é a lista com os numeros multiplicados: {resultado}")



if __name__ == '__main__':
    main()
