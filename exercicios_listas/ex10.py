# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

import random

lista_numeros1 = []
lista_numeros2 = []
lista_numeros3 = []

for i in range(10):
    numero_lista_1 = random.randrange(1, 30)
    numero_lista_2 = random.randrange(1, 30) 
    lista_numeros1.append(numero_lista_1)
    lista_numeros2.append(numero_lista_2)
    lista_numeros3.append(numero_lista_1)
    lista_numeros3.append(numero_lista_2)

print(lista_numeros1)
print(lista_numeros2)
print(lista_numeros3)