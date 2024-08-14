'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
count_par = 0
count_impar = 0
for i in range(10):
    numero = int(input('Digite o numero a ser verificado: '))

    if numero % 2 == 0:
        count_par += 1
    else:
        count_impar += 1

print(f'A quantidade de números pares é de: {count_par} e a quantidade de números impares é de: {count_impar}')