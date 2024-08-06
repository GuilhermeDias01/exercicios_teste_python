# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

import sys
data_usuario = input('Digite a data no formado dd/mm/aaaa: ')

dd = int(data_usuario[0:2])
mm = int(data_usuario[3:5])
aaaa = int(data_usuario[6:10])

if dd < 1 or dd > 31:
    print(f'O dia {dd} é inválido')
elif mm < 1 or mm > 12:
    print(f'O mês {mm} é inválido')
elif aaaa < 1 or aaaa > 9999:
    print(f'O ano {aaaa} é inválido')
else:
    print(f'A data {dd}/{mm}/{aaaa} é válida.')

