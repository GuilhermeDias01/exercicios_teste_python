# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range(5):

    numero_adicionado = float(input('Digite o numero '))

    soma += numero_adicionado
    media = soma / 5

print(f'A soma dos números é de: {soma} e a média é de {media:.2f}')