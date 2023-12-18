#01. Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira,
#3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.

def domingo(dom):
    return "domingo"

def segunda(seg):
    return "segunda-feira"

def terca(ter):
    return "terça-feira"

def quarta(qua):
    return "quarta-feira"

def quinta(qui):
    return "quinta-feira"

def sexta(sex):
    return "sexta-feira"

def sabado(sab):
    return "sábado"

def semana(dias):
    if dias == "1":
        return domingo(dias)
    elif dias == "2":
        return segunda(dias)
    elif dias == "3":
        return terca(dias)
    elif dias == "4":
        return quarta(dias)
    elif dias == "5":
        return quinta(dias)
    elif dias == "6":
        return sexta(dias)
    elif dias == "7":
        return sabado(dias)
    else:
        return "valor inválido"

def main():
    print("digite um número e exiba o dia correspondente da semana, de 1 a 7. (1-domingo, 2-segunda-feira, 3-terça-feira etc.)")
    dias = input()

    resultado = semana(dias)

    print(f"É {resultado}")

if __name__ == "__main__":
    main()
