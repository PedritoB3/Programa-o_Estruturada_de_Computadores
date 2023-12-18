def frase(P):
    palavras = len(P)
    return palavras

def main():
    print("Digite qualquer frase, e mostrará o numero de caracteres, mas o diferencial é que os espaços em branco no inicio ou no final da frase não contam")
    P = input().strip()
    caractere = frase(P)

    print(f"O numero de caracteres é de: {caractere}")

if __name__ == '__main__':
    main()

