largura = float(input("Digite a largura da parede: ")) 
altura = float(input("Digite a altura da parede: "))
area = largura * altura

print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².")

# A conta para cada 2 metros de área é: o valor em metros da área dividido por 2

qtd_tinta = area / 2

print(f"Para pintar essa parede, será necessário {qtd_tinta}L de tinta.")