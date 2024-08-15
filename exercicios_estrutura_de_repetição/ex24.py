# Faça um programa que calcule o mostre a média aritmética de N notas.

media = int(input('Informe a quantidade de notas a serem inseridas: '))
count = 0
notas = []
total_notas = 0

media_total = 0
while count < media:
    
    nota = float(input('Informe o valor da nota: '))
    notas.append(nota)
    count +=1

for nota in notas:
    total_notas += nota

media_total = total_notas / media

print(media_total)