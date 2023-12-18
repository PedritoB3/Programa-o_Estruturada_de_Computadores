#Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual
#delas é a mais recente.

def data1(d1,m1,a1):
    return d1,m1,a1
def data2(d2,m2,a2):
    return d2,m2,a2

def main():
    print("Digite duas datas")
    print("Digite a primeira:")
    d1 = input("Digite o dia").strip()
    m1 = input("Digite o mês").strip()
    a1 = input("Digite o ano").strip()
    print("Agora a segunda data:")
    d2 = input("Digite o dia").strip()
    m2 = input("Digite o mês").strip()
    a2 = input("Digite o ano").strip()

    dt1 = data1(d1,m1,a1)
    dt2 = data2(d2,m2,a2)

    if dt1 > dt2:
        print(f"A data 1 é a mais recente:{d1}/{m1}/{a1}")
    elif dt2 > dt1:
        print(f"A data 2 é a mais recente:{d2}/{m2}/{a2}")
    elif dt1 == dt2:
        print(f"Ambas as datas são iguais:{d1}/{m1}/{a1}")

if __name__ == "__main__":
    main()

