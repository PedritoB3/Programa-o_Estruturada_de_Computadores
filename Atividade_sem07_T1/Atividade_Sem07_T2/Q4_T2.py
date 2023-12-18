def data(dia,mes):
  if (mes == 3 and dia >=21) or (mes == 4 and dia <= 19):
      return "Áries"
  if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    return "Touro"
  if (mes == 5 and dia >=21) or (mes == 6 and dia <= 21):
      return "Gêmeos"
  if (mes == 6 and dia >=22) or (mes == 7 and dia <= 22):
      return "Câncer"
  if (mes == 7 and dia >=23) or (mes == 8 and dia <= 22):
      return "Leão"
  if (mes == 8 and dia >=23) or (mes == 9 and dia <= 22):
      return "Virgem"
  if (mes == 9 and dia >=23) or (mes == 10 and dia <= 22):
      return "Libra"
  if (mes == 10 and dia >=23) or (mes == 11 and dia <= 21):
     return "Escorpião"
  if (mes == 11 and dia >=22) or (mes == 12 and dia < 22):
      return "Sagitário"
  if (mes == 12 and dia >=22) or (mes == 1 and dia <= 19):
      return "Capricórnio"
  if (mes == 1 and dia >=20) or (mes == 2 and dia <= 18):
      return "Aquário"
  if (mes == 2 and dia >=19) or (mes == 3 and dia <= 20):
      return "Peixes"

def main():
    print("Iremos saber qual será seu signo.")
    print("Digite o dia:")
    dia = int(input())
    print("Digite o mês:")
    mes = int(input())
    signo = data(dia,mes)

    print(f"Seu signo é o {signo}")
if __name__ == '__main__':
    main()
