#1. As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
#estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
#a) len(), que recebe uma lista e retorna número de itens;
#b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
#c) min(),que recebe uma lista e retorna o menor valor
#d) max(), que recebe uma lista retorna o maior valor
#e) sum(), que recebe uma lista retorna a soma dos valores
#Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a
#leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o
#resultado encontrado.
#Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(),
#minimo(), maximo(), soma().

def funcao_comprimento(numero):
    quantidade = 0
    for i in range(numero):
        quantidade += 1
    return quantidade

def funcao_inverter(funcao,numero):
    funcao_invertida = []
    for i in range(numero):
        funcao_invertida.append(funcao[-i-1])
    return funcao_invertida

def funcao_minimo(funcao,numero):
    outra_funcao_minima = funcao[0]
    for i in range(numero):

        if outra_funcao_minima > funcao[i]:
            outra_funcao_minima = funcao[i]

    return outra_funcao_minima

def funcao_maxima(funcao,numero):
    funcao_maxima = funcao[0]
    for i in range(numero):

        if funcao_maxima < funcao[i]:
            funcao_maxima = funcao[i]

    return funcao_maxima

def funcao_soma(funcao,numero):
    soma = 0

    for i in range(numero):
        soma += funcao[i]

    return soma

def funcao_zero():
    funcao = []
    numero = 0
    while True:
        numero_entrada = int(input("Digite numeros aleatorios. E digite 0 para terminar:"))

        if numero_entrada == 0:
            break
        else:
            numero += 1
            funcao.append(numero_entrada)
    return funcao,numero



def main():
    funcao,numero = funcao_zero()

    quantidade = funcao_comprimento(numero)

    inverter = funcao_inverter(funcao,numero)

    minimo = funcao_minimo(funcao,numero)

    maximo = funcao_maxima(funcao,numero)

    soma = funcao_soma(funcao,numero)

    print(f"Esta é a lista: {funcao}\nEsta é a quantidade: {quantidade}\nEsta é a lista invertida: {inverter}\nEste é o minimo: {minimo}\nEste é o maximo: {maximo}\nEsta é a soma: {soma}")


if __name__ == "__main__":
    main()
