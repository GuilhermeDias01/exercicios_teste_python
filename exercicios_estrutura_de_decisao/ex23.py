# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

valor_usuario = float(input('Digite o valor a ser verificado: '))

valor_usuario_round = round(valor_usuario, 2)

if valor_usuario == valor_usuario_round:
    print('Inteiro')
else:
    print('Decimal')