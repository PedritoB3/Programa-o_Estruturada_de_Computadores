def caractere(ca):
    caractere = ord(ca)
    return caractere

def main():
    print("Coloque um unico caractere, e dirá qual será seu codigo numerico:")
    ca = input()
    print(f"O codigo numerico ao caractere correspondido é o {caractere(ca)}")

if __name__ == '__main__':
    main()
