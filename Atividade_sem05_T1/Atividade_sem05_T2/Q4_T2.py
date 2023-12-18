def caractere(c):
    return c

def main():
    print("Insira uma letra ou numero, caso coloque outro caractere(como simbolo), será considerado como falso:")
    c = input().strip()
    LN = "abcdefghijklmnopqrstuvwxyz0123456789""ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    resultado = caractere(c) in LN

    print(resultado)
if __name__ == '__main__':
    main()

