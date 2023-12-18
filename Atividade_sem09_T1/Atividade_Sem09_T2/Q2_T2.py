#02. Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas,
#dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores
#e o ponto “.” no final da frase. Exemplos:

#• 521 = cinco centenas, duas dezenas e uma unidade.
#• 107 = uma centena e sete unidades.
#• 80 = oito dezenas.

def em_extenso(num):
    unidades = ["", "uma unidade", "duas unidades", "tres unidades", "quatro unidades", "cinco unidades", "seis unidades", "sete unidades", "oito unidades", "nove unidades"]
    dezenas = ["", "uma dezena", "duas dezenas", "tres dezenas", "quatro dezenas", "cinco dezenas", "seis dezenas", "sete dezenas", "oito dezenas", "nove dezenas"]
    centenas = ["", "uma centena", "duas centenas", "tres centenas", "quatro centenas", "cinco centenas", "seis centenas", "sete centenas", "oito centenas", "nove centenas"]
    extenso = ""

    return unidades,dezenas,centenas,extenso


def calculo_em_extenso(numero):
    unidades,dezenas,centenas,extenso = em_extenso(numero)

    if int(numero) < 1 or int(numero) >= 1000:
        return ""

    centena = numero // 100 % 10
    dezena = numero // 10 % 10
    unidade = numero // 1 % 10

    if centena > 0:
        extenso += centenas[centena]
    if centena == 100:
        extenso+="cem"


    if centena > 0 and dezena == 0 and unidade == 0:
        extenso += ""
    elif centena > 0 and dezena > 0 and unidade == 0:
        extenso += " e "
    elif centena > 0 and dezena == 0 and unidade > 0:
        extenso += " e "
    elif centena > 0 and dezena > 0 and unidade > 0:
        extenso += ", "

    if dezena > 0:
        extenso += dezenas[dezena]
    if dezena > 0 and unidade == 0:
        extenso += ""
    elif dezena > 0 and unidade > 0:
        extenso += " e "

    if unidade > 0:
        extenso += unidades[unidade]
    if unidade > 0:
        extenso += ""


    return extenso

def numero_permitido(numero):
    extenso = calculo_em_extenso(numero)
    return f"{extenso}."

def main():
    print("digite um número inteiro menor que 1000 e mostrarei por extenso a quantidade de centenas,dezenas e unidades do número:")
    numero = int(input())

    resultado = numero_permitido(numero)

    print(f"{numero} = {resultado}")

if __name__ == "__main__":
    main()


