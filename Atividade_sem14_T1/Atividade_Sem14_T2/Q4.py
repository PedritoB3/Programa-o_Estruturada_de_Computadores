def expressao_numerica(funcao_x, funcao_y):
    expressao = ""
    total = 0
    for i in range(5):
            if i > 0:
                expressao += " + "
            expressao += f"({funcao_x[i]} x {funcao_y[i]})"
            total += funcao_x[i] * funcao_y[i]

    return f"{expressao} = {total}"

def funcao():
    funcao_x = []
    funcao_y = []

    for i in range(5):
        entrada_usuario = int(input())
        funcao_x.append(entrada_usuario)

    for i in range(5):
        entrada_usuario = int(input())
        funcao_y.append(entrada_usuario)

    return funcao_x, funcao_y

def main():
    funcao_x, funcao_y = funcao()

    resultado = expressao_numerica(funcao_x,funcao_y)

    print(f"{funcao_x}\n{funcao_y}\n{resultado}")


if __name__ == "__main__":
    main()
