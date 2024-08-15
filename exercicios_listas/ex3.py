# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

qntd_notas = 4
count = 1
lista_de_notas = []
nota_total = 0

while count <= qntd_notas:
    nota = float(input(f'Informe a nota de Nº{count}: '))
    lista_de_notas.append(nota)
    count += 1

for nota in lista_de_notas:
    nota_total += nota

media_total = nota_total / qntd_notas

print(f'As notas informadas foram: {lista_de_notas}')
print(f'E a média é de: {media_total}')
