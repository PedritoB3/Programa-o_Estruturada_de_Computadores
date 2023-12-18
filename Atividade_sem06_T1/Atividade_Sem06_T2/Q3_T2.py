def maca_e_banana(valor_ma,valor_ba):
    maca = (valor_ma*3)
    banana = (valor_ba*2)
    valor_total = (maca+banana)
    return valor_total

def main():
    print("Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total!")
    print("insira o valor da maÇa")
    vm = float(input())
    print("insira o valor da banana")
    vb = float(input())
    resultado = maca_e_banana(vm,vb)

    print(f"Esse é o valor total de sua compra: R${resultado:0.2f}")

if __name__ == '__main__':
    main()
