def calcular(a,b,c):
    return 2 * a + 5 * b-c

def main():
    print("Insira três valores diferentes para a expressão '2*a+5*b-c'")
    num1 = int(input("A:").strip())
    num2 = int(input("B:").strip())
    num3 = int(input("C:").strip())
    print("O valor da expressão é:")
    print(f"{calcular(num1,num2,num3)}")

if __name__ == '__main__':
    main()


