def valor(v):
    return v % 2 == 1
def resposta(re):
    if valor(re):
        bool(True)
    elif valor(re) == 0:
        bool(False)
    else:
        bool(False)
    return valor(re)

def main():
    print("Insira um numero impar, caso contrario, será considerado como falso:")
    re = float(input())
    resultado = resposta(re)

print(resultado)
if __name__ == '__main__':
    main()
