import math

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = (cateto_adjacente * cateto_adjacente) + (cateto_oposto * cateto_oposto)

print(f"O valor da hipotenusa é: {math.sqrt(hipotenusa):.2f}")