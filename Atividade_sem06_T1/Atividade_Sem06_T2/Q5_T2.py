def pinguin(Celsius):
    Fahrenheit = (Celsius*(9/5))+32
    return Fahrenheit

def main():
    print("Digite uma temperatura em Celsius, e assim será convertida em Fahrenheit")
    Celsius = float(input())
    resultado = pinguin(Celsius)
    print(f"{resultado:.2f}ºF, essa é a temperatura em Fahrenheit")

if __name__ == '__main__':
    main()
