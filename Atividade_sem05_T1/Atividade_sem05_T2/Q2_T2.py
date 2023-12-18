def caractere(c):
    return c

def main():
    print("Insira uma letra, caso coloque outro caractere, será considerado como falso:")
    c = input().strip()
    letra = "abcdefghijklmnopqrstuvwxyz""ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    resultado = caractere(c) in letra

    print(resultado)
if __name__ == '__main__':
    main()

