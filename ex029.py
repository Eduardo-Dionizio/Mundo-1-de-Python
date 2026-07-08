velocidade_atual = int(input("Qual é a sua velocidade atual? "))
limite_velocidade = 80
multa = 7.00

if velocidade_atual > 80:
    formula = (velocidade_atual - limite_velocidade) * multa
    print(f"MULTADO!! Você excedeu o limite de velocidade.")
    print(f"Você será multado em: R${formula:.2f}")

else:
    print(f"Bom dia!! Diriga com cuidado.")