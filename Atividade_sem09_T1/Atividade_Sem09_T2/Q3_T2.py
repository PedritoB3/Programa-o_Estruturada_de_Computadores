#03. Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.
#OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas;
#Considere que em anos bissextos o mês de fevereiro tem 29 dias.

def anobissexto(numero):
    return ((numero % 4 == 0) and (numero % 100 != 0) or (numero % 400 == 0))
def data10(entrada):
    if (len(entrada) == 8):
     dia = int(entrada[:2])
     mes = int(entrada[2:4])
     ano = int(entrada[4:])
     return dia,mes,ano

def data(numero):
    dia, mes, ano = data10(numero)

    if (anobissexto(ano)):
        fevereiro = 29
    else:
        fevereiro = 28

    if ((1 <= mes <= 12) and (1 <= dia <= 31)):
        if (mes == 2):
            return 1 <= dia <= fevereiro
        else:
            if (mes in [4, 6, 9, 11]):
                return 1 <= dia <= 30
            else:
                return 1 <= dia <= 31
    else:
        return False

def main():
    print("digite uma data no formado DDMMAAA e informarei se é uma data válida ou não.")
    numero = str(input())

    resultado = data(numero)
    print(f"A data é {resultado}")

if __name__ == "__main__":
    main()


