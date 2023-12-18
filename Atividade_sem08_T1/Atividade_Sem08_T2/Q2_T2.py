#02. Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e
#100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.

def operacao(n):
    return n//10, n % 10
def digitos(n):
    n, ultimo = operacao(n)
    soma = ultimo

    if n < 10000:
        n, ultimo = operacao(n)
        soma += ultimo
    if n < 1000:
        n, ultimo = operacao(n)
        soma += ultimo
    if n < 100:
        n, ultimo = operacao(n)
        soma += ultimo
    if n < 10:
        n, ultimo = operacao(n)
        soma += ultimo
    if n < 1:
        n, ultimo = operacao(n)
        soma += ultimo

    if n == 0:
        return soma
    else:
        return -1

def main():
    print("Escreva um numero inteiro de 1 a 100mil, e retornará com a soma dos digitos. Exemplo: 12.476 deve mostrar a 20.")
    n = int(input().strip())

    soma = digitos(n)

    print(f'A soma dos digitos é de {soma}')

if __name__ == "__main__":
    main()
