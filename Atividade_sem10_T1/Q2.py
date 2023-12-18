#02.Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade de números pares e números ímpares contidos no mesmo.



def numeros_par_impar(conjunto):
    par = 0
    impar = 0
    for i in range(1,101):
        num = int(input())
        if num%2 == 0:
            par +=1
        elif num%2 == 1:
            impar +=1
    print(f"Esta é a quantidade de numeros par: {par}")
    print(f"Esta é a quantidade de numeros impar:{impar}")

def main():
    conjunto = 0
    print("Digite 100 numeros diferentes:")
    resultado = numeros_par_impar(conjunto)

if __name__ == '__main__':
    main()
