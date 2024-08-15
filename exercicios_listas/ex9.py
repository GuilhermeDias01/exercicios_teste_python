# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

import random

lista_numeros = []
soma = 0
numero = 0

for i in range(10):
    numero = random.randrange(1, 10) ** 2
    lista_numeros.append(numero)


for j in lista_numeros:
    soma += j 

print(soma)
    