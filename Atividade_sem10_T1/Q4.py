#04.Escreva um programa que gere a seguinte sequência: 10, 20, 30, 40, ..., 990, 1000. Considere a separação dos números por vírgula seguido de espaço em brando e o pontos no final da sequência.

def sequencia(seq):
    numeros = ''

    for n in range(10,1010,10):
        numeros += str(n)+', '
    numeros = numeros[:-2]+'.'

    return numeros.strip()

def main():
    numero = 1
    print("Essa é a sequencia de numeros com virgula:")
    resultado = sequencia(numero)

    print(resultado)


if __name__ == "__main__":
    main()
