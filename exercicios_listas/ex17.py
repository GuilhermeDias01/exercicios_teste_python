'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''
import sys


lista_de_saltos = [] 
lista_da_ordem_saltos = ['Primeiro Salto', 'Segundo Salto','Terceiro Salto','Quarto Salto','Quinto Salto',]

while True:
    nome = input('Informe o nome COMPLETO do competidor: ')

    if nome == "":
        print('Nome incorreto, o programa será encerrado!')
        sys.exit()

    for i in range(0, 5):
        salto = float(input('Informe o valor do '+str(lista_da_ordem_saltos[i])+': '))
        lista_de_saltos.append(salto)

    print('')
    print('Atleta: '+str(nome)+'')
    print('')
    for i in range(0,5):
        print(''+str(lista_da_ordem_saltos[i])+': '+str(lista_de_saltos[i])+' m')
    print('')
    print('Resultado final:')
    print('Atleta: '+str(nome)+'')
    print(f'Saltos: ', end='') 
    print(' - '.join(str(valor) for valor in lista_de_saltos), end='')
    print('')
    print(f'Media dos saltos: {(sum(lista_de_saltos) / 5):.1f} m')

    break