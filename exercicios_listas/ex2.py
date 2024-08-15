# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = [1,2,3,4,5,6,7,8,9,10]

lista.reverse()

print(lista)

# or 

lista2 = []

for i in range(1,11):
    lista2.append(i)

for numero in lista2[::-1]:
    print(numero)