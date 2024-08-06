# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano_informado = int(input('Informe o ano: '))

if ano_informado % 4 == 0:
    print('O ano informado é bissexto')
else:
    print('O ano informado não é bissexto.')