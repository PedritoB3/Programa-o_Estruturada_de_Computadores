def caractere(c):
    return c

def main():
    print("Insira uma vogal, caso coloque outro caractere, será considerado como falso:")
    c = input().strip()
    vogais = "aeiou""AEIOU"

    resultado = caractere(c) in vogais

    print(resultado)
if __name__ == '__main__':
    main()

