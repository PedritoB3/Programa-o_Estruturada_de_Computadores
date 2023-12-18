altura = float(input("Coloque o valor da altura:").strip())
comprimento = float(input("Coloque o alor do comprimento:").strip())
largura = float(input("Coloque o valor da largura:").strip())

area_do_piso_da_sala = largura * comprimento
volume_da_sala = largura * comprimento * altura
area_das_paredes_da_sala = 2 * altura * largura+2 * altura * comprimento
print(area_do_piso_da_sala)
print(volume_da_sala)
print(area_das_paredes_da_sala)
