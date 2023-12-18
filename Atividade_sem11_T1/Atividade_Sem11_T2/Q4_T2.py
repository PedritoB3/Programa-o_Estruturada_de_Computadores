def cardapio():
    total_compra = 0
    while True:
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        pedido = input().upper() [0]

        if pedido == "H":
            total_compra += 5.50

        elif pedido == "C":
            total_compra += 6.80

        elif pedido == "M":
            total_compra += 4.50

        elif pedido == "A":
            total_compra += 7.00

        elif pedido == "Q":
            total_compra += 4.00

        elif pedido == "X":
            return total_compra

        else:
            print("Opção inválida.")

def main():
    resultado = cardapio()

    print(f"{resultado:.2f}")

if __name__ == "__main__":
    main()
