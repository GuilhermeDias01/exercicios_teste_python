# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_de_caracteres = []
count = 0
contador2 = 0

while count < 10:
    caracter = input('Digite o caracter a ser verificado: ')
    if caracter.upper() == 'A' or caracter.upper() == 'E' or caracter.upper() == 'I' or caracter.upper() == 'O' or caracter.upper() == 'U':
        count += 1
    else:
        lista_de_caracteres.append(caracter)
        count += 1
        contador2 += 1

print(f'A quantidade de consoantes lidas foi de: {contador2} e as consoantes são: {lista_de_caracteres}')