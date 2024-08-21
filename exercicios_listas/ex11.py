# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

import random

lista_numeros1 = []
lista_numeros2 = []
lista_numeros3 = []
lista_numeros4 = []

for i in range(10):
    
    numero_lista_1 = random.randrange(1, 30)
    numero_lista_2 = random.randrange(1, 30) 
    numero_lista_3 = random.randrange(1, 30) 

    lista_numeros1.append(numero_lista_1)
    lista_numeros2.append(numero_lista_2)
    lista_numeros3.append(numero_lista_3)

    lista_numeros4.append(numero_lista_1)
    lista_numeros4.append(numero_lista_2)
    lista_numeros4.append(numero_lista_3)

print(lista_numeros1)
print(lista_numeros2)
print(lista_numeros3)
print(lista_numeros4)