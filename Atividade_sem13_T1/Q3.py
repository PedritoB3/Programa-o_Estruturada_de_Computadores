#3. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
#a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro)
#casas decimais.
#b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa
#decimal. Se n = 0, imprima “SEM NOTAS”.
#c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
#Dica: certifique-se de ler apenas um caractere com input()[0]

def num_reais(n):
    lista = []

    if n == 0:
        return lista

    else:
        for i in range(n):
            usuario_entrada = float(input())
            usuario_entrada = round(usuario_entrada, 4)
            lista.append(usuario_entrada)
        lista.reverse()

    return lista

def notas(n):
    lista = []
    soma = 0

    if n == 0:
        return lista, "SEM NOTAS"

    else:
        for i in range(n):
            usuario_entrada = float(input())
            usuario_entrada = round(usuario_entrada,1)
            soma += usuario_entrada
            lista.append(usuario_entrada)

    media = soma/n
    media = round(media,1)

    return lista,media

def letras(n):
    lista = []
    vogais = 0
    letra_vogais = "aeiouAEIOU"

    if n == 0:
        return lista,vogais

    else:

        for i in range(n):
            usuario_entrada = str(input()[0])
            lista.append(usuario_entrada)

            if usuario_entrada in letra_vogais:
                lista.remove(usuario_entrada)
                vogais+=1

    return lista,vogais

def main():
    n = int(input())


    numero_reais = num_reais(n)
    lista_notas,media = notas(n)
    lista_letras,vogais = letras(n)

    print(f"{numero_reais}\n{lista_notas}\n{media}\n{vogais}\n{lista_letras}")

if __name__ == "__main__":
    main()
