# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

# ex:1
for numero in range(21):
    print(numero)

# ex:2

numeros = ""
for i in range(1, 20):
    numeros += f"{i}, "
numeros += "20"

print(numeros)