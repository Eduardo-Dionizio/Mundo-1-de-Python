frase = input("Digite uma frase: ")

print(f"A letra a aparece: {frase.count('a')} vezes")
print(f"A letra a aparece a primeira vez no índice: {frase.find('a')}")
print(f"A letra a aparece a última vez no índice: {frase.rfind('a')}")