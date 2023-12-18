def sequencia(numero):
    primeiro_numero = -1
    segundo_numero = 1
    quantidade_numero = 0
    resposta = ''
    while numero >= 2:
        terceiro_numero = primeiro_numero + segundo_numero
        resposta += f"{terceiro_numero}, "

        primeiro_numero = segundo_numero
        segundo_numero = terceiro_numero

        quantidade_numero += 1

        if quantidade_numero == numero:
            return resposta[:-2]



def main():
    numero = int(input())

    resultado = sequencia(numero)

    print(f"{resultado}")

if __name__ == "__main__":
    main()

