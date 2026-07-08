frase = '   Aprenda Python  '

# Transformacao
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())

frase2 = "Curso em Video Python"
# Separar strings em formato de lista
dividido = frase2.split()
print(dividido)
print(dividido[0])
# Fazer a junção
print('-'.join(dividido))