frase = 'Curso em Vídeo Python'

# Quantidade - sendo caracteres, elemento em listas etc.
print(len(frase))
# Quantas vezes aparece
print(frase.count('o', 0, 14))
# Quantas vezes encontrou começando pelo indíce indicado. -1 indica que não existe
print(frase.find('deo'))
print('Curso' in frase)