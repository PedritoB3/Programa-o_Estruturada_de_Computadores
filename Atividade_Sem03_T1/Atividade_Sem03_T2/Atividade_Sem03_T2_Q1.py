r = float(input("Coloque o valor de R, raio:".strip()))

comprimento_da_circunferencia = format(2*3.141592*r, ".6f")
area_do_circulo = format(3.141592*r**2, ".6f")
area_da_esfera = format(4*3.141592*r**2, ".6f")
volume_da_esfera = format(4/3*3.141592*r**3, ".6f")
print("Comprimento da circunferencia:")
print(comprimento_da_circunferencia)
print("Area do circulo:")
print(area_do_circulo)
print("Area da esfera:")
print(area_da_esfera)
print("Volume da esfera:")
print(volume_da_esfera)