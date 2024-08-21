# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

import random
import copy

lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro']
lista1 = []
lista_com_mes_e_temp_mensal = []
total_temperaturas = 0
count = 1

for mes in lista_meses:
    lista1.append(mes)
    lista1.append(int(random.randrange(20, 30)))
    lista_com_mes_e_temp_mensal.append(copy.deepcopy(lista1))
    lista1.clear()

for listas in lista_com_mes_e_temp_mensal:
    for i, valor in enumerate(listas):
        if i == 1:
            total_temperaturas += valor

media_temp_anual = round(total_temperaturas / len(lista_meses))

print(f'A média anual é de: °{media_temp_anual} C.')
print(f'Abaixo podemos ver o mês e a temperatura dos mêses onde as temperaturas ficaram acima da média anual:')

for listas in lista_com_mes_e_temp_mensal:
    for i, valor in enumerate(listas):
        if i == 1 and valor > media_temp_anual:
            print(f'{count} - {listas[0]}, °{listas[1]} C.')
            count += 1