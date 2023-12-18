def sinal(cor):
    if cor.upper() == "V":
       return "Siga"
    elif cor.upper() == "A":
       return "Atenção"
    elif cor.upper() == "E":
       return "Pare"

def main():
    print("Insira a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho):")
    cor = input()
    resultado = sinal(cor)

    print(resultado)
if __name__ == '__main__':
    main()
