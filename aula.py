dias = int(input("Quantos dias para a entrega: "))
valor = int(input("Qual o valor do produto: "))

if dias > 7 or valor < 100:
    print("Prioridade Baixa")
elif dias <= 7 and dias >= 4 or valor >= 100 and valor <= 500:
    print("Prioridade Média")
elif dias < 4 or valor > 500:
    print("Prioridade Alta")