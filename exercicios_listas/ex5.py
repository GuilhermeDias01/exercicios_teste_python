# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

import random

lista_numeros = []
lista_numeros_pares = []
lista_numeros_imapres = []

count = 0

while count < 20:
    numero =  random.randrange(0, 100)
    lista_numeros.append(numero)
    count += 1
    
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_numeros_pares.append(numero)
    else:
        lista_numeros_imapres.append(numero)

print(lista_numeros)
print(lista_numeros_pares)
print(lista_numeros_imapres)
