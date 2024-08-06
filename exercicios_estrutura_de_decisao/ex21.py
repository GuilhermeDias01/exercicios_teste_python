'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

import sys

valor_saque = int(input('Informe o valor que deseja sacar entre R$10.00 e R$600.00: '))

if valor_saque < 10 or valor_saque > 600:
    sys.exit()

notas_de_100 = valor_saque // 100
valor_saque = valor_saque - (notas_de_100 * 100)

notas_de_50 = valor_saque // 50
valor_saque = valor_saque - (notas_de_50 * 50)

notas_de_10 = valor_saque // 10
valor_saque = valor_saque - (notas_de_10 * 10)

notas_de_5 = valor_saque // 5
valor_saque = valor_saque - (notas_de_5 * 5)

notas_de_1 = valor_saque // 1
valor_saque = valor_saque - (notas_de_1 * 1)

if notas_de_100 > 0:
    print(f"{notas_de_100} nota(s) de cem")
if notas_de_50 > 0:
    print(f"{notas_de_50} nota(s) de cinquenta")
if notas_de_10 > 0:
    print(f"{notas_de_10} nota(s) de dez")
if notas_de_5 > 0:
    print(f"{notas_de_5} nota(s) de cinco")
if notas_de_1 > 0:
    print(f"{notas_de_1} nota(s) de um")