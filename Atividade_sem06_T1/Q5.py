def roupa(valor):
    vista = float(valor-(valor*9/100))
    semjuros = float(valor/5)
    comjuros = float(valor+(valor*17/100))/10
    return vista, semjuros, comjuros

def main():
    print("Coloque o valor aleatorio de uma compra:")
    vis = float(input())

    v,s,c = roupa(vis)

    print(f"O valor para pagamento á vista, com desconto de 9% é de: {v:0.2f}")
    print(f"O valor da prestação para pagamento em 5 vezes, sem desconto nem juros é de: {s:0.2f}")
    print(f"Valor da prestação para pagamento em 10 vezes, com 17% de juros é de: {c:0.2f}")

if __name__ == '__main__':
    main()

