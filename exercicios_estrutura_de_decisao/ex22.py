# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.


valor = int(input('Digite o numero inteiro: '))

if valor % 2 == 0:
    print(f'O numero {valor} é um numero par.')
else:  
    print(f'O numero {valor} é um numero impar.')