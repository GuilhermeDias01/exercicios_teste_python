'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

string_1 = input('Digite o conteúdo da string 1: ')
string_2 = input('Digite o conteúdo da string 2: ')

conta_carc_string_1 = len(string_1)
conta_carc_string_2 = len(string_2)

print(f'String 1: {string_1}')
print(f'String 2: {string_2}')

print(f'Tamanho de "{string_1}": {conta_carc_string_1} caracteres.')
print(f'Tamanho de "{string_2}": {conta_carc_string_2} caracteres.')

if conta_carc_string_1 == conta_carc_string_2:
    print('As duas strings são de tamanhos iguais')
else:
    print('As duas strings são de tamanhos diferentes.')

if string_1 == string_2:
    print('As duas strings possuem conteúdo iguais')
else:
    print('As duas strings possuem conteúdo diferente')