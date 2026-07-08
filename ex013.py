salario = float(input("Qual é o salário do funcionário? R$"))
reajuste = salario * 0.15

salario_atual = salario + reajuste

print(f"Um funcionário ganhava R${salario}, com 15% de aumento, passa a receber R${salario_atual:.2f}")
