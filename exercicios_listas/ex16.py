'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''
import random

lista_com_valores = [('$200 - $299'), ('$300 - $399'), ('$400 - $499'), ('$500 - $599'), ('$600 - $699'), ('$700 - $799'), ('$800 - $899'), ('$900 - $999'), ('$1000 em diante')]
lista_com_contadores = [0] * 9
quantidade_vendedores = int(input('informe a quantidade de vendedores: '))
lista_de_salarios = []

for i in range(0, quantidade_vendedores):
    valor = int(random.randrange(0, 15000))
    lista_de_salarios.append(round(200 + (valor * 0.09)))

for salario in lista_de_salarios:
    indice = salario // 100 - 2
    indice_maximo = len(lista_com_contadores)-1
    indice = min(indice, indice_maximo)
    lista_com_contadores[indice] += 1

for j, valor in enumerate(lista_com_contadores):
    print('O Número de funcionários com salário de '+str(lista_com_valores[j])+ ' é igual a: '+str(lista_com_contadores[j]))