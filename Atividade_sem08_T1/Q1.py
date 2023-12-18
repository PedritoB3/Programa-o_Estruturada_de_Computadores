#01. Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de
#nascimento de uma pessoa, calcule e escreva a idade exata em anos
def anos(da,ma,aa,dp,mp,ap):
    subtracao = int(aa-ap)
    if da<dp or ma<mp or aa<ap:
        return int(subtracao-1)
    elif da>dp or ma>mp or aa>ap:
         return int(subtracao)

def main():
    da = int(input("Escreva o dia atual:"))
    ma = int(input("Escreva o mês atual:"))
    aa = int(input("Escreva o ano atua:"))
    print("agora sua data de nascimento.")
    dp = int(input("Escreva o dia:"))
    mp = int(input("Escreva o mês:"))
    ap = int(input("Escreva o ano:"))

    resultado = anos(da,ma,aa,dp,mp,ap)
    print(f"Essa é sua idade exata:{resultado}")

if __name__ == "__main__":
    main()

