def area_e_perimetro(L):
 area = float(L**2)
 perimetro = float(L*4)
 return area, perimetro

def main():
 print("Insira o valor do 'lado' de um quadrado:")
 L = float(input().strip())

 a, p = area_e_perimetro(L)
 print("O valor será mostrado em 4 casas decimais alinhado a direita e com 10 espaços na tela.")
 print("A área do quadrado é:")
 print(f"{a:10.4f}")
 print("A área do perímetro é:")
 print(f"{p:10.4f}")

if __name__ == '__main__':
    main()

