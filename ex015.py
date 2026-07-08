km_percorridos = int(input("Quantos kms foram percorridos: "))
dias_aluguel = int(input("Quantos dias foram utilizados: "))

valor_total = (km_percorridos * 0.15) + (dias_aluguel * 60)

print(f"O valor total do aluguel é de R${valor_total:.2f}")