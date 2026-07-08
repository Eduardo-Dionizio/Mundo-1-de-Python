# Ao importar bibliotecas: O import pega tudo dela, from .... import pega apenas o que você pediu
import math
num = int(input("Digite um número: "))

raiz_quadrada = math.sqrt(num)

print(f"Raiz quadrada de {num}: {raiz_quadrada:.2f}")
