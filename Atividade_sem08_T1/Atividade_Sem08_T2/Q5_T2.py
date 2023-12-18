#Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:
#Média Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Média Exercícios) / 7
#A atribuição dos conceitos obedece a tabela abaixo.
#Conceito |Média Final
#:---------:|:--------------:
#A | >= 9.0
#B | >= 7.5 e < 9.0
#C | >= 6.0 e < 7.5
#D | >= 4.0 e < 6.0
#E | < 4.0
#O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.



def matricula(MA):
    return MA

def media_final(n1,n2,n3,ME):
    media_final = float((n1+n2*2+n3*3+ME)/7)
    return media_final

def situacao(media_final):
    resultado = media_final
    if resultado >= 9.0:
        return '\nA' '\nAprovado'
    elif resultado >= 7.5 and resultado < 9.0:
        return '\nB' '\nAprovado'
    elif resultado >= 6.0 and resultado < 7.5:
        return '\nC' '\nAprovado'
    elif resultado >= 4.0 and resultado < 6.0:
        return '\nD' '\nReprovado'
    elif resultado < 4.0:
        return '\nE' '\nReprovado'

def main():
     print("Digite sua matricula de aluno:")
     MA = input().strip()
     print("Agora digite as suas notas em 3 provas:")
     n1 = float(input("Nota 1:").strip())
     n2 = float(input("Nota 2:").strip())
     n3 = float(input("Nota 3:").strip())
     print("Agora digite a sua média das notas obtida nos exercicios:")
     ME = float(input())

     matricula_do_aluno = matricula(MA)
     operacao = media_final(n1,n2,n3,ME)
     resultado = situacao(operacao)

     print(f'Sua matricula: {matricula_do_aluno}\nSua media final e situação:{operacao:.2f}{resultado} ')

if __name__ == "__main__":
    main()
