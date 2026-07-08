import random

lista_alunos = ["João", "Bento", "Nicholas", "Hugo"]

aluno1, aluno2, aluno3, aluno4 = random.sample(lista_alunos, 4)

print("Ordem de apresentação: ")
print(f'Primeiro: {aluno1}')
print(f'Segundo: {aluno2}')
print(f'Terceiro: {aluno3}')
print(f'Quarto: {aluno4}')