def pessoas():
    idade_total = 0
    numero_pessoas = 0
    maior_idade = 0
    menor_idade = 150


    while True:
        idade_pessoa = int(input())

        if idade_pessoa == 0:
            break

        if idade_pessoa > 0:
            idade_total += idade_pessoa
            numero_pessoas += 1

        if idade_pessoa > maior_idade:
            maior_idade = idade_pessoa

        if idade_pessoa < menor_idade:
            menor_idade = idade_pessoa


    idade_media = idade_total/numero_pessoas
    return numero_pessoas,idade_media,maior_idade,menor_idade

def main():
    numero_pessoas,idade_media,maior_idade,menor_idade = pessoas()

    print(f"{numero_pessoas}\n{idade_media:.2f}\n{menor_idade}\n{maior_idade}")

if __name__ == "__main__":
    main()


