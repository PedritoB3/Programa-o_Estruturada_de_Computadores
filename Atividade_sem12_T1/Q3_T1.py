def pais(popu_B,popu_A):
    taxa_A = 2/100
    taxa_B = 3/100
    temp_ano = 0
    variavel_substituta = 0

    if popu_B > popu_A:
      variavel_substituta = popu_A
      popu_A = popu_B
      popu_B = variavel_substituta

    while True:
        if popu_B < popu_A:
            temp_ano += 1
            popu_A += popu_A * taxa_A
            popu_B += popu_B * taxa_B

        if popu_B >= popu_A:
            return temp_ano

def main():
    popu_B = int(input())
    popu_A = int(input())

    resultado = pais(popu_B,popu_A)

    print(f"{resultado}")

if __name__ == "__main__":
    main()

