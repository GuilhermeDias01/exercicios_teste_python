'''
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
'''

nome = input('Digite seu nome: ')

for i in range(len(nome)):
    print(nome[i:i+1:])