# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import random

lista_numeros = []
soma = 0
multiplica = 1

for i in range(5):
    numero = random.randrange(1, 250)
    lista_numeros.append(numero)
    soma += numero
    multiplica *= numero

print(lista_numeros)
print(soma)
print(multiplica)

