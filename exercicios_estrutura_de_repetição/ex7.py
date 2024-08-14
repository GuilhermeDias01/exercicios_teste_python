# Faça um programa que leia 5 números e informe o maior número.

confere_numero = 0

for i in range(5):

    numero_adicionado = float(input('Digite o numero '))

    if numero_adicionado > confere_numero:
        confere_numero = numero_adicionado

print(f'O Maior numero é: {confere_numero}')