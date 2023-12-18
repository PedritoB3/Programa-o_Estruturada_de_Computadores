#01.Escreva um programa que mostre todos os números inteiros de 1 a 50 (um por linha).


def sequencia(numero):
    for i in range(1,51):
        print(f"{i}")

def main():
    numero = 0
    print("Esta é a sequencia de numeros de 1 até 51:")
    resultado = sequencia(numero)

if __name__ == '__main__':
    main()

