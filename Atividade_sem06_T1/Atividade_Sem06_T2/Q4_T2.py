def zob(ano):
    idade = ano//2
    return idade

def main():
    print("Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais!")
    print("Insira uma idade em anos terrestres:")
    idade = int(input())
    idade_final = zob(idade)

    print(f"zob tem {idade_final} anos espaciais.")

if __name__ == '__main__':
    main()
