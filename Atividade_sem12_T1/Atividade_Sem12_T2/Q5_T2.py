def numero_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
def main():

    x = int(input())
    y = int(input())

    for num in range(x, y + 1):
        if numero_primo(num):

            print(f"{num}")

if __name__ == "__main__":
    main()
