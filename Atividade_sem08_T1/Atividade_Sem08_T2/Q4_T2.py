#04. Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para ‘homens’ e 2 para ‘mulheres’.
#Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
#• para homens: (72.7 * altura) – 58
#• para mulheres: (62.1 * altura) – 44.7
def peso_ideal(altura,s):
    if s == 1:
       return float(72.7*altura)-58
    elif s == 2:
        return float(62.1*altura)-44.7

def main():
    print("Digite sua altura:")
    altura = float(input().strip())
    print("Agora digite seu sexo, considere 1 para ‘homens’ e 2 para ‘mulheres’.")
    sexo = int(input().strip())

    resposta = peso_ideal(altura,sexo)

    print(f'O peso ideal baseando na altura e no sexo é de {resposta:.2f}Kg')

if __name__ == "__main__":
    main()

