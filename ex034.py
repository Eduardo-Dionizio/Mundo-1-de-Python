salario = float(input("Funcionario, digite seu salário: "))

if salario > 1250:
    salario = salario + (salario * 0.10)
    print(f"Parabéns. Seu salário aumentou 10%, totalizando: R${salario:.2f}")

else:
    salario = salario + (salario * 0.15)
    print(f"Parabéns. O seu salário aumentou 15%, totalizando: R${salario:.2f}")