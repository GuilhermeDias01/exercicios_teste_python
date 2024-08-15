# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
import random

media_do_alunos = []
contador= 0

for aluno in range(10):
    soma_das_notas = 0

    for nota in range(4):
        nota = random.randrange(0, 10)
        soma_das_notas += nota

    media = soma_das_notas / 4
    media_do_alunos.append(media)

for media in media_do_alunos:
    if media >= 7:
        contador += 1
    else:
        ...
    
print(f'A quantidade de alunos com a média maior ou igual a zero é de {contador}')
print(media_do_alunos)

