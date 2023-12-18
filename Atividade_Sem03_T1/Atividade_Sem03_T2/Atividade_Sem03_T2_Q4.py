horas_totais = int(input("Coloque o valor de horas totais/Ex:160 min :").strip())
horas = int((horas_totais/60))
minutos = (horas_totais % 60)
print(f"{horas}h{minutos}min")
