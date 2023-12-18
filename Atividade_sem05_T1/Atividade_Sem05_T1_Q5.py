def numero(a,b,c,d):
 return str(d+c+b+a)

def main():
 print("Insira o valor de um número inteiro entre 1000 a 9999:")
 a, b, c, d = input().strip()

 numero(a,b,c,d)

 print("Este é o valor na ordem inversa:")
 print(numero(a,b,c,d))

if __name__ == '__main__':
    main()
