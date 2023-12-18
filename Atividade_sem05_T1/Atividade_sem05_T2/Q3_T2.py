def caractere(c):
    return c

def main():
    print("Insira uma consoante, caso coloque outro caractere, será considerado como falso:")
    c = input().strip()
    consoante = "bcdfghjklmnpqrstvwxyz""BCDFGHJKLMNPQRRSTVWXYZ"


    resultado = caractere(c) in consoante

    print(resultado)
if __name__ == '__main__':
    main()

