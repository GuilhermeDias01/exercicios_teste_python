'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''
import random
lista_com_valores = []

for i in range(0,100):
    numero = random.randrange(1,7)
    lista_com_valores.append(numero)

for i in range(1,7):
    print(f'O numero {i} apareceu {lista_com_valores.count(i)} vezes.')    
