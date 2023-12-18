produto = float(input("Coloque o preco do produto:").strip())
desconto = produto*0.10
valor = format(produto-desconto, ".2f")
print(f"O preco do valor com desconto de 10% será de {valor}")
