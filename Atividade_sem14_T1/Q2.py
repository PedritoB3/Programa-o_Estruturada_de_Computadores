#2. Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe
#uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo
#count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2
#aparece na lista.
#Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois
#o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.

def verificacao(funcao,numero):
    numero_entrada = int(input("Digite um numero da sua lista:"))
    quantidade = 0
    for i in range(numero):
        if numero_entrada == funcao[i]:
            quantidade += 1

    return numero_entrada,quantidade


def lista_funcao():
    funcao = []
    numero = 0
    while True:
        numero_entrada = int(input("Digite numeros aleatorios. Digite 0 para encerrar: "))
        if numero_entrada == 0:
            break
        else:
            numero += 1
            funcao.append(numero_entrada)
    return funcao,numero


def main():
    funcao, numero = lista_funcao()

    numero_entrada,contador = verificacao(funcao,numero)

    print(f"Sua lista: {funcao}\nO seu numero: {numero_entrada}\nQuantidade que repetiu:{contador}")


if __name__ == "__main__":
    main()
