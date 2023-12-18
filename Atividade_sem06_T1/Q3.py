def segundos(seg):
    horas = seg//3600
    segundos = seg%3600
    minutos = segundos//60
    segundos = segundos%60
    return horas, minutos, segundos

def main():
    print("Coloque uma quantidade de segudnos, que logo será convertido em horas,minutos e segundos:")
    s = int(input())
    ho,min,seg = segundos(s)
    print(f"São {ho}:{min}:{seg}")

if __name__ == '__main__':
    main()


