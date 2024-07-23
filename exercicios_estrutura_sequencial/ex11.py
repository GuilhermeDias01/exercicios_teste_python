#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto cdo dobro do primeiro om metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

valor1_usuario = input('Digite o primeiro valor inteiro: ')
valor2_usuario = input('Digite o segundo valor inteiro: ')
valor3_usuario = input('Digite o valor real: ')

saida1 =  (2 * int(valor1_usuario) * (int(valor2_usuario) / 2)) 
print(f'A primeira saida é: {saida1}')

saida2 = (3 * int(valor1_usuario) + int(valor3_usuario))
print(f'A segunda saida é: {saida2}')

saida3 = (int(valor3_usuario)**3)
print(f'A terceira saida é: {saida3}')