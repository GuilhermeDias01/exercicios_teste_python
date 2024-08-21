'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''

def imprime_numero(numero):
    for i in range (numero):
        i += 1
        print(' '.join(str(i)* i))

numero_usuario = int(input('Digite o numero: '))

imprime_numero(numero_usuario)