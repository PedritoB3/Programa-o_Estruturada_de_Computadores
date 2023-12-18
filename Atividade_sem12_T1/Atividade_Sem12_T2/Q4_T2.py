def numero_primo(num):
    divisor = True
    if num <= 1:
        divisor = False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                divisor = False
                break
    return divisor


def main():
    num = int(input())

    resultado = numero_primo(num)

    print(f"{resultado}")

if __name__ == "__main__":
    main()
