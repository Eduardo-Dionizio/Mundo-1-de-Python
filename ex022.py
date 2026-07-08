nome_completo = input("Digite o seu nome completo: ").strip()

nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()

nome_dividido = nome_completo.split()
nome_juncao = ''.join(nome_dividido)

print(f"Nome em maisculo: {nome_maiusculo}")
print(f"Nome minusculo: {nome_minusculo}")


print(f"Quantidade de letras do nome: {len(nome_juncao)}")
print(f"Quantidade de letras do primeiro nome: {len(nome_dividido[0])}")
