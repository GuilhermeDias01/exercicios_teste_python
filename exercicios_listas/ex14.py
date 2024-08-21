'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

lista_perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?" , "Devia para a vítima?" ,"Já trabalhou com a vítima?"]
contador = 0

for pergunta in lista_perguntas:
    resposta = input(f'{pergunta} Responda com [S] para sim e [N] para não: ')
    if resposta.upper() == 'S':
        contador += 1

if contador <= 2:
    print('Suspeita')
elif contador == 3 or contador == 4: 
    print('Cúmplice')
else:
    print('Assassino')