nome_completo = input("Digite seu nome completo: ")

nome_separado = nome_completo.split()
print(f"Primeiro nome: {nome_separado[0]}")
print(f"Ultimo nome: {nome_separado[-1]}")