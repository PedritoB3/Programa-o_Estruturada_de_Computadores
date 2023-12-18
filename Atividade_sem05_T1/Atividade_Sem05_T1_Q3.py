def preco_original(P, vp):
 preco_com_acrescimo = float(P+(P*(vp/100)))
 preco_com_desconto = float(P-(P*(vp/100)))
 return preco_com_acrescimo, preco_com_desconto

def main():
 print("Insira o valor de um preço:")
 P = float(input().strip())

 print("Insira um valor percentual:")
 vp = float(input().strip())

 pa, pd = preco_original(P,vp)

 print("OBS:O valor será mostrado em duas casas decimais.")
 print("O valor com acrescimo é:")
 print(f"{pa:0.2f}")
 print("O preço com o desconto percentual é:")
 print(f"{pd:0.2f}")

if __name__ == '__main__':
    main()

