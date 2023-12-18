#1. Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

def soma(numero):
    soma = 0
    for i in range(10):
        soma += numero[i]
    return soma

def multiplicacao(numero):
    multiplicacao = 1
    for i in range(10):
        multiplicacao *= numero[i]
    return multiplicacao
def main():
    lista = []
    contador = 0
    while True:
        numero = int(input(f"Digite uma lista de 10 numeros, {contador+1} numeros escrito:  "))
        contador += 1
        lista.append(numero)
        if contador == 10:
            break

    resultado_soma = soma(lista)
    resultado_multi = multiplicacao(lista)
    print(f"da lista de {lista} numeros\nEssa é a soma entre eles:{resultado_soma}\nEssa é a multiplicação entre eles:{resultado_multi}")

if __name__ == '__main__':
    main()
