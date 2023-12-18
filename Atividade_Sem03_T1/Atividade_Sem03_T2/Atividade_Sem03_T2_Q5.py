tempo_de_servico = float(input("Coloque o valor do tempo de serviço de um funcionario:").strip())
bonus_por_ano = float(input("Agora o valor de bonus por ano que ele trabalhou:").strip())
funcionario = format(tempo_de_servico*bonus_por_ano, ".2f")
print("Esta será a bonificação do funcionario:", funcionario)
