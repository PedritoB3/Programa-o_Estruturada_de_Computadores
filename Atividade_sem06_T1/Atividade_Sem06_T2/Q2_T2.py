def transacao_financeira(tr):
    return round(tr)

def main():
    print('Insira uma quantidaade de dinheiro, e iremos arredondar para um valor mais proximo')
    tr = float(input())
    resultado = transacao_financeira(tr)

    print(f"O valor arredondado é: {resultado}")

if __name__ == '__main__':
    main()
