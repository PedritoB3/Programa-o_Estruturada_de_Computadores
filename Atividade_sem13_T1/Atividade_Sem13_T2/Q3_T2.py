#3. Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que
#tem nota maior ou igual a 6 (seis).

def verificacao(lista):
    lista_nota = []
    for i in range(50):
        if lista[i] >= 6:
            lista_nota.append(i)

    return lista_nota
def main():
    lista = []

    for i in range(50):
        usuario_entrada = float(input(f"Coloque a nota de {i+1}/50 alunos: "))
        lista.append(usuario_entrada)

    lista_nota = verificacao(lista)

    print(f"Esta é lista com os índices dos alunos que tem nota maior ou igual a 6: {lista_nota}")

if __name__ == '__main__':
    main()
