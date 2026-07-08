import random

numero_aleatorio = random.randint(1, 5)
eu = int(input("Qual é o número aleatório? "))

if eu == numero_aleatorio:
    print(f"Parabéns! Você acertou o número {numero_aleatorio}")
else:
    print("Que pena. Você errou.")