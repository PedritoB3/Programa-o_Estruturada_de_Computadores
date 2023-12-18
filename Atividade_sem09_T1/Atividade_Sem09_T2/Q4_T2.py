#Um sacolão está vendendo frutas com a seguinte tabela de preços:

#Até 5Kg Acima de 5Kg
#Morango R$ 2,50 por Kg R$ 2,20 por Kg
#Maça R$ 1,80 por Kg R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
#desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade
#(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


def calculo(morango, maca):
    if morango <= 5:
        valmo = 2.50
    else:
        valmo = 2.20
    if (maca <= 5):
        valma = 1.80
    else:
        valma = 1.50

    valTotal = (valmo * morango) + (valma * maca)

    if (morango + maca > 8) or (valmo + valma > 25):
        return round(valTotal * 0.90, 2)
    else:
        return round(valTotal, 2)


def main():
    print("digite a quantidade (em Kg) de morangos:")
    morango = float(input())
    print("Agora digite quantidade (em Kg) de maças:")
    maca = float(input())

    resultado = calculo(morango, maca)

    print(f"Esse é o valor a ser pago: {resultado:.2f}")

if __name__ == "__main__":
    main()
