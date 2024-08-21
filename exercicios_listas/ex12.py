# Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random

idades = []
alturas = [1.70, 1.56, 1.67, 1.72, 1.85 , 1.90, 1.59, 1.68, 1.70, 1.64, 1.78, 1.69, 1.75, 1.71, 1.65, 1.67, 1.73, 1.81, 1.83, 1.66, 1.57, 1.63, 1.79, 1.87, 1.82, 1.54, 1.52, 1.65, 
           1.61, 1.70]
soma_alturas = 0
count_13anos_altura_menor_media = 0

for i in range(1, 30):
    idades.append(random.randrange(10, 18))

for altura in alturas:
    soma_alturas += altura

media = soma_alturas / len(alturas)
print(f'{media:.2f}')

for i, idade in enumerate(idades):
    if idade > 13 and alturas[i] < media:
       count_13anos_altura_menor_media += 1

print(f'A quantidade de alunos com mais 13 e altura inferior a média de {media:.2f} é de: {count_13anos_altura_menor_media}')