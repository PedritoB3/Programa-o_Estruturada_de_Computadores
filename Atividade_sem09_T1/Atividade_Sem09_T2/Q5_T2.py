#05. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a) "Telefonou para a vítima ?"
#b) "Esteve no local do crime ?"
#c) "Mora perto da vítima ?"
#d) "Devia para a vítima ?"
#e) "Já trabalhou com a vítima ?"

#Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa
#no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4
#como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def contador(Q1, Q2, Q3, Q4, Q5):
    Respostas_positivas = 0
    if (Q1.upper() == "S"):
        Respostas_positivas += 1
    if (Q2.upper() == "S"):
        Respostas_positivas += 1
    if (Q3.upper() == "S"):
        Respostas_positivas += 1
    if (Q4.upper() == "S"):
        Respostas_positivas += 1
    if (Q5.upper() == "S"):
        Respostas_positivas += 1

    return Respostas_positivas


def interrogatorio(Q1, Q2, Q3, Q4, Q5):
    Respostas_positivas = contador(Q1, Q2, Q3, Q4, Q5)

    if (Respostas_positivas == 2):
        return "Suspeito"
    if (3 <= Respostas_positivas <= 4):
        return "Cúmplice"
    if (Respostas_positivas == 5):
        return "Assassino"
    else:
        return "Inocente"


def main():
    print("Agora iremos começar o interrogatorio, digite só 'S' ou 'N' para as perguntas.")
    print("Telefonou para a vítima ?:")
    pergunta1 = input().strip()
    print("Esteve no local do crime ?:")
    pergunta2 = input().strip()
    print("Mora perto da vítima ?:")
    pergunta3 = input().strip()
    print("Devia para a vítima ?:")
    pergunta4 = input().strip()
    print("Já trabalhou com a vítima ?:")
    pergunta5 = input().strip()

    resultado = interrogatorio(pergunta1,pergunta2,pergunta3,pergunta4,pergunta5)

    print(f"Resultado final, você foi considerado como {resultado}")

if __name__ == "__main__":
    main()
