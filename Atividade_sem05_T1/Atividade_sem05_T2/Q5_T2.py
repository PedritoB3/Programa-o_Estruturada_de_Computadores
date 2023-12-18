def caractere(c):
    return c

def main():
    print("Insira um simbolo(como !@#$), caso coloque outro caractere, será considerado como falso:")
    c = input().strip()
    LN = "!@#$%¨&*()_-=+{[}]?/"


    resultado = caractere(c) in LN

    print(resultado)
if __name__ == '__main__':
    main()

