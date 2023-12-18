def perguntas(res1,res2,res3):
    pontuacao = 0

    if res1 == 'a':
        pontuacao += 1
        print("Pergunta 1: você acertou")
    elif res1 in 'bcde':
        print("Pergunta 1: você errou")

    if res2 == 'c':
        pontuacao += 1
        print("Pergunta 2: você acertou")
    elif res2 in 'abde':
        print("Pergunta 2: você errou")

    if res3 == 'c':
        pontuacao += 1
        print("Pergunta 3: você acertou")
    elif res3 in 'abde':
        print("Pergunta 3: você errou")

    if pontuacao == 3:
        return f"Muito bem, você acertou todas as questões, essa é sua pontuação: {pontuacao}"
    elif pontuacao < 3:
        return f"Que pena, você não acertou todas as questões, tente novamente, essa é sua pontuação: {pontuacao} pontos"

def main():
    print("Seja bem-vindo(a) ao meu quiz bem simples, são três perguntas facéis, cada uma valendo 1 ponto.")

    print("Pergunta 1: Quantos Planeta Terra cabem dentro do Sol?")
    print("A)Um milhão\nB)Cem\nC)Seiscentos\nD)Cento e cinquenta\nE)Dois milhões")
    res1 = input("Resposta:").lower().strip()

    print("\nPergunta 2: Em que lugar vivem mais cangurus do que pessoas?")
    print("A)Indonésia\nB)Nova Zelândia\nC)Australia\nD)Papua-Nova-Guiné\nE)África do Sul.")
    res2 = input("Resposta:").lower().strip()

    print("\nPergunta 3:Quantos olhos a maior parte das aranhas têm?")
    print("A)Dois\nB)Quatro\nC)Quatro pares\nD)Seis\nE)Um")
    res3 = input("Resposta:").lower().strip()

    pontuacao = perguntas(res1,res2,res3)
    print(pontuacao)

if __name__ == '__main__':
    main()

