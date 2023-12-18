#04. Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a
#média. Considere duas casas decimais.
def media(n1,n2,n3,n4,n5):
    media = float((n1+n2+n3+n4+n5)/5)
    maior = [n for n in [n1, n2, n3, n4, n5] if n > media]
    return media, maior

def main():
    n1 = int(input("Digite o valor 1:").strip())
    n2 = int(input("Digite o valor 2:").strip())
    n3 = int(input("Digite o valor 3:").strip())
    n4 = int(input("Digite o valor 4:").strip())
    n5 = int(input("Digite o valor 5:").strip())

    resultado, maior  = media(n1,n2,n3,n4,n5)

    print(f"Essa é a média: {resultado:.2f}")
    for num in maior:
        print(f"E esse é o valor maior que a media:\n{num}")

if __name__ == "__main__":
    main()
