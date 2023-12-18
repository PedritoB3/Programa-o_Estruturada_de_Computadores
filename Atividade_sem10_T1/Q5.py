#04.Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.

def conjunto(maior):
    numeros = []
    for n in range(100):
        numero = int(input())
        numeros.append(numero)

    resultado = max(numeros)
    print(f"Esse é o maior valor dentre os 100 nummeros diferentes: {resultado}")
def main():
   numero = 0
   print("Digite 100 numeros diferentes:")
   resultado = conjunto(numero)
if __name__ == "__main__":
    main()
