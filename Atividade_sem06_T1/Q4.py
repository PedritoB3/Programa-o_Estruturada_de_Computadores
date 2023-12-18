def numeros_maiores(num1,num2,num3,num4,num5):
    maior = max(num1,num2,num3,num4,num5)
    return maior

def numeros_menores(num1,num2,num3,num4,num5):
    menor = min(num1,num2,num3,num4,num5)
    return menor


def media_aritimetica(num1,num2,num3,num4,num5):
 media = float((num1+num2+num3+num4+num5)/5)
 return media

def main():
    print("Digite 5 numeros aleatorios diferentes:")
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    n5 = float(input())

    mai = numeros_maiores(n1,n2,n3,n4,n5)
    men = numeros_menores(n1,n2,n3,n4,n5)
    med = media_aritimetica(n1,n2,n3,n4,n5)

    print(f"O maior numero lido dentre os cincos lidos é: {mai}")
    print(f"O menor numero lido dentre os cincos lidos é: {men}")
    print(f"A media aritimetica dos cincos numeros é: {med}")

if __name__ == '__main__':
    main()
