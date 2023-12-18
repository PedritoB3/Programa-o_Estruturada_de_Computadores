#03.T2 Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 e parando em 250 ou antes 99 bugs no software, pegue um deles e conserte... Tecle “Ctrl+F5” 106 bugs no software, pegue um deles e conserte... Tecle “Ctrl+F5” 113 bugs no software, pegue um deles e conserte... Tecle “Ctrl+F5” ... Vamos fazer mais um café!

def cancao(num):
    for n in range(99,251,7):
        numeros = int(n)
        print(f"{numeros} bugs no software, pegue sete deles e conserte...")
        print('Tecle "Ctrl+F5"')
    print("Vamos fazer mais um café!")

def main():
    numero = 0
    cancao(numero)

if __name__ == "__main__":
    main()
