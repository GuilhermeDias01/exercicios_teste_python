'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''
import random
import sys

lista_de_notas = []
verifica = True
soma_das_notas = 0
quantidade_valores_acima_media = 0
quantidade_valores_abaixo_de_7 = 0

while verifica:
    nota = random.randrange(-1, 10)

    if nota == -1 and len(lista_de_notas) == 0:
        lista_de_notas.append(random.randrange(1, 10))
    elif nota == -1 and len(lista_de_notas) >= 1:
        verifica = False
    elif nota != 0 and nota != -1:
        lista_de_notas.append(nota)
    
for valor in lista_de_notas:
    soma_das_notas += valor 
    

media_das_notas = soma_das_notas / len(lista_de_notas)  

for valor in lista_de_notas:
    if valor > media_das_notas:
        quantidade_valores_acima_media += 1

    if valor < 7:
        quantidade_valores_abaixo_de_7 += 1


print(f'A quantidade de valores lidas foi de: {len(lista_de_notas)}.')
print('')
print('Segue os valores na ordem inserida: ')
print(', '.join(str(valor) for valor in lista_de_notas), end='')   
print('')
print('')
print('Segue os valores na ordem inversa: ')
for valor in reversed(lista_de_notas):
    print(valor)
print('')
print(f'A soma dos valores é de: {soma_das_notas}')
print('')
print(f'A média dos valores é de: {media_das_notas:.2f}')
print('')
print(f'A quantidade de valores a cima da média é de: {quantidade_valores_acima_media}')
print('')
print(f'A quantidade de valores abaixo do valor 7 é de: {quantidade_valores_abaixo_de_7}')
print('')
print('O programa está sendo ENCERRADO.')

sys.exit()




