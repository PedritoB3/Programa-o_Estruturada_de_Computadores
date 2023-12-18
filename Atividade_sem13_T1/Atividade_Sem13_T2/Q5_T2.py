#5. Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa
#deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
#IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e
#retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso. Por exemplo:

def esta_ordenado(lista):
   if lista == sorted(lista):
       return "LISTA ORDENADA"
   else:
       return "LISTA NÃO ORDENADA"


def main():
    lista = []
    numero = int(input("Digite uma quantidade de numeros: "))
    for i in range(numero):

        usuario_entrada = str(input(f"Digite {i+1}/{numero} de numeros: ")).strip()
        lista.append(usuario_entrada)

    lista_ordenada = esta_ordenado(lista)

    print(f"A lista é {lista_ordenada}")

if __name__ == '__main__':
    main()
