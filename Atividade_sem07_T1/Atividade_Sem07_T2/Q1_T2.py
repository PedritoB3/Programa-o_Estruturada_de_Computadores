def caracteres(nome1,nome2=""):
    total_caracteres = len(nome1)+len(nome2)
    return total_caracteres
def numero(num):
    return num

def main():
    print("Digite o seu nome:")
    nome = input().strip()
    print("Agora digite o seu estado civil, sendo '1' para casado e '2' para solteiro")
    num = int(input().strip())
    estado_civil = numero(num)

    if estado_civil == 1:
        print("Como você é casado, digite o nome do seu cônjuge:")
        conjuge = input().strip()
        total_caracteres = caracteres(nome,conjuge)
        print(f"Esse é o total de caracteres do seu nome e do seu cônjuge: {total_caracteres}")
    elif estado_civil == 2:
        total_caracteres = caracteres(nome)
        print(f"Como você é solteiro, esse será o total de caractere de só seu nome:{total_caracteres}")

if __name__ == '__main__':
    main()
