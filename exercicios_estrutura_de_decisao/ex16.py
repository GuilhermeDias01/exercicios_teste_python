'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import sys
import math

valor_a = float(input('informe o valor de A: '))

if valor_a == 0:
    print('O valor de A não pode ser 0')
    sys.exit()
else:
    print('Aqui1') 

valor_b = float(input('informe o valor de B: '))
valor_c = float(input('informe o valor de C: '))

delta = (valor_b ** 2) - ((4 * valor_a) * valor_c)

if delta < 0:
    print('O Delta é menor que 0, por isso não possui raizes.')
    sys.exit()
elif delta == 0:
       valor_x = ((-valor_b ) / 2 * valor_a)
       print(f'Delta é zero. O valor de X é: {valor_x}')
else:
       valor_x1 = (-valor_b + math.sqrt(delta)) / 2 * valor_a
       valor_x2 = (-valor_b - math.sqrt(delta)) / 2 * valor_a

       print(f'O valor de X é: {valor_x1:.0f} e {valor_x2:.0f}')
 

  
