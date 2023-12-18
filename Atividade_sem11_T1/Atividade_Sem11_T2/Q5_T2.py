def nota_final():
     while True:
        nota = float(input())
        if (nota > 10 or nota < 0):
            print("Nota inválida.")

        elif (8.5 <= nota <= 10):
            return "A"

        elif (7.0 <= nota < 8.5):
            return "B"

        elif (5.0 <= nota < 7.0):
            return "C"

        elif (4.0 <= nota < 5.0):
            return "D"

        else:
            return "E"

def main():

    resultado = nota_final()

    print(f"{resultado}")

if __name__ == "__main__":
    main()
