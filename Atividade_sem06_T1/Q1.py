def nome(n):
 nomes = len(n)
 return nomes

def main():
 print("Coloque um nome aleatorio, e dirá quantos caracteres tem:")
 n = input()
 nome_pedido = nome(n)
 print(f"Esse nome tem {nome_pedido} caracteres")

if __name__ == '__main__':
    main()
