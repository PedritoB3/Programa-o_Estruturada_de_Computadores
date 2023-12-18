#4. Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura
#dos jogadores, determine:
#a. o nome e a altura do jogador mais alto;
#b. a média de altura do time;
#c. os jogadores com altura superior à média, listando o nome e a altura de cada um.

def jogador_alto(funcao_nome,funcao_altura):
    funcao_alto = funcao_altura[0]
    funcao_jogador = funcao_nome[0]

    for i in range(12):
       if funcao_alto < funcao_altura[i]:
           funcao_alto = funcao_altura[i]
           funcao_jogador = funcao_nome[i]

    return funcao_alto,funcao_jogador


def funcao_media(funcao_altura):
    soma_altura = 0

    for i in range(12):
        soma_altura += funcao_altura[i]

    media = soma_altura/12
    return media

def funcao_media_superior(funcao_nome,funcao_altura):
    media = funcao_media(funcao_altura)

    print(f"JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME:")
    for i in range(12):
       if media < funcao_altura[i]:
          print(f"{funcao_nome[i]}\n{funcao_altura[i]:.2f}")

def funcao_time():
    funcao_nome = []
    funcao_altura = []

    for i in range(12):
        nome = input(f"Jogador {i+1}, digite o nome:")
        altura = float(input("Agora digite a altura deste jogador: "))

        funcao_nome.append(nome)
        funcao_altura.append(altura)
    return funcao_nome,funcao_altura

def main():
    nome,altura = funcao_time()

    alto,jogador = jogador_alto(nome,altura)

    media = funcao_media(altura)

    print(f"JOGADOR MAIS ALTO DO TIME:\n{jogador}\n{alto:.2f} ")
    print(f"ALTURA MÉDIA DO TIME:\n{media:.2f}")
    funcao_media_superior(nome,altura)

if __name__ == "__main__":
    main()

