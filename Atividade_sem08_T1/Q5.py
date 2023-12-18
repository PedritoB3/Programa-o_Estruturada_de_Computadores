#O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso
#ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está
#em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e
#calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

def resposta(peso,altura):
    calculo = float(peso/(altura*altura))
    return calculo

def IMC(calculo):
    resultado = calculo
    if resultado < 18.5:
        return "Abaixo do peso"

    elif resultado < 25:
        return "Peso normal"

    elif resultado < 30:
        return "Sobrepeso"

    elif resultado < 35:
        return "Obeso leve"

    elif resultado < 40:
        return "Obeso moderado"

    elif resultado >= 40:
        return "Obeso mórbido"

def main():
    peso = float(input("Digite seu peso: ").strip())
    altura = float(input("Digite sua altura: ").strip())

    resultado_calculo = resposta(peso,altura)
    resultado_final = IMC(resultado_calculo)

    print(f"Esse é o seu IMC:{resultado_calculo:.2f}\nE você está {resultado_final}")
if __name__ == "__main__":
    main()

