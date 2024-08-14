# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = int(input('Digite o numero: '))
count = 0

for i in range(n):
    if n % (i+1) == 0:
        count += 1

if count == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')

