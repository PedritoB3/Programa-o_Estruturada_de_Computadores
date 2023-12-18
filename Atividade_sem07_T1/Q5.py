def soma(n1,n2,n3):
  if n3 > 8:
     return ((n1+n2+n3)/3)+1
  else:
    return (n1+n2+n3)/3

def main():
    print("Insira três notas, correspondente a nota de um aluno:")
    n1 = float(input("Nota 1:").strip())
    n2 = float(input("Nota 2:").strip())
    n3 = float(input("Nora 3,caso seja maior que 8, receberar um ponto na media:").strip())

    resultado = float(soma(n1,n2,n3))
    if resultado > 9:
     resultado = 10

    print(f"A media da sua nota é de {resultado:.2f}.")

if __name__ == '__main__':
    main()


