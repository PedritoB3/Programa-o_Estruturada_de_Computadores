#5. Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais
#alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a
#altura arredondando para duas casas decimais.

def verificacao(nomes_alunos,idades_alunos,altura_alunos,media):
    for i in range(30):
        if idades_alunos[i] > 13:
            if altura_alunos[i] < round(media,2):
                print(f"{nomes_alunos[i]}")

def funcao_alunos():
    nomes_alunos = []
    idades_alunos = []
    altura_alunos = []
    soma = 0

    for i in range(30):
        nomes = input(f"\nDigite o nome do aluno {i+1}: ")
        idades = int(input(f"Agora a idade do aluno {i+1}: "))
        alturas = float(input(f"Agora a altura do aluno {i+1}: "))

        nomes_alunos.append(nomes)
        idades_alunos.append(idades)
        altura_alunos.append(alturas)
        soma += altura_alunos[i]

    media = round(soma/30, 2)


    return nomes_alunos,idades_alunos,altura_alunos,media

def main():
    nomes,idades,alturas,media = funcao_alunos()

    print(f"MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    verificacao(nomes,idades,alturas,media)

if __name__ == "__main__":
    main()
