#Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. O programa deve
#inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a
#palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes
#a altura) do retângulo. Separe esses valores com um hífen.
def valores(base,altura):
    perimetro = (base*2)+(altura*2)
    area = (base*altura)
    if base == altura:
        return "QUADRADO"
    else:
        return f"O perimetro é {perimetro} - e a área é {area}"

def main():
    print("Caso o valor da base e da altura sejam iguais, é um quadrado, se for diferentes, um retângulo.")
    print("Digite o valor da base:")
    base = int(input())
    print("Digite o valor da altura:")
    altura = int(input())

    poligono = valores(base,altura)

    print(f"{poligono}")

if __name__ == "__main__":
    main()



