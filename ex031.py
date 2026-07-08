viagem = int(input("Qual vai ser a distância da sua viagem em km? "))
viagens_pequenas = 0.5
viagens_longas = 0.45

print(f"Você esta prestes a começar uma viagem de {viagem}km")

if viagem <= 200:
    formula = viagem * viagens_pequenas
    print(f"E o preço da sua passagem será de: R${formula:.2f}")
else:
    formula = viagem * viagens_longas
    print(f"E o preço da sua passagem será de: R${formula:.2f}")
