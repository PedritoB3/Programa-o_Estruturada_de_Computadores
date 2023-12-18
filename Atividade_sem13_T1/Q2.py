
#Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
#a) preencha com 0 (zero) e imprima a lista;
#b) preencha com os números de 1 a n e imprima a lista;
#c) preencha com valores inteiros lidos pelo teclado e imprima a lista;
#d) preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert
#para sempre incluir os elementos no início da lista;

def lis_zero(n):
    lista_zero = []
    zero = 0
    for i in range(n):
        zero *= n
        lista_zero.append(zero)
    return lista_zero

def val_usuario(n):
    lista_usuario = []

    for i in range(1,n+1):
        lista_usuario.append(i)
    return lista_usuario


def main():
    n = int(input())
    lista = []
    lista_inversa = []

    for i in range(n):
        usuario_entrada = int(input())
        lista.append(usuario_entrada)

    for i in range(n):
        usuario_entrada = int(input())
        lista_inversa.append(usuario_entrada)

    lista_zero = lis_zero(n)
    valor_usuario = val_usuario(n)

    print(f"{lista_zero}\n{valor_usuario}\n{lista[:n]}\n{lista_inversa[n::-1]}")


if __name__ == '__main__':
    main()
