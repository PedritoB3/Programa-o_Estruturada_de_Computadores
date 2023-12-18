def dodo(popu_inicial):
    ano = 1599
    popu_total = popu_inicial
    while popu_total >= 0.1*popu_inicial:
        ano += 1
        popu_nascimento = popu_total * 0.01
        popu_morte = popu_total * 0.06

        popu_total += popu_nascimento-popu_morte

        print(f"{ano:.0f},{popu_nascimento:.0f},{popu_morte:.0f},{popu_total:.0f}")

def main():
    popu_inicial = int(input())
    dodo(popu_inicial)

if __name__ == "__main__":
    main()





