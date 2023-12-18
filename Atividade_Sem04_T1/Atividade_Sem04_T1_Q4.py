hora = int(input("Coloque o valor de hora:").strip())*3600
minuto = int(input("Coloque o valor de minuto:").strip())*60
segundo = int(input("Coloque o valor de segundo").strip())
meia_noite = (hora+minuto+segundo)
print(f"{meia_noite}segundos se passaram no total desde a última meia-noite")
