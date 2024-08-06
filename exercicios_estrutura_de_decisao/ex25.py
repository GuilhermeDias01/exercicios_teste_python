'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

print('Para as perguntras abaixo, responda "S" para sim e "N" para não:')

resposta1 = input('Telefonou para a vítima?').upper()
resposta2 = input('Esteve no local do crime?').upper()
resposta3 = input('Mora perto da vítima?').upper()
resposta4 = input('Devia para a vítima?').upper()
resposta5 = input('Já trabalhou com a vítima?').upper()

contador = 0 

if resposta1 == 'S':
    contador += 1

if resposta2 == 'S':
    contador += 1

if resposta3 == 'S':
    contador += 1

if resposta4 == 'S':
    contador += 1

if resposta5 == 'S':
    contador += 1

if contador < 2:
    print("Inocente")
elif contador == 2:
    print("Suspeita")
elif contador < 5:
    print("Cúmplice")
else:
    print("Assassino")