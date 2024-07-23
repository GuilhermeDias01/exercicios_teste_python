# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temp_celsius_usuario = input('Digite a temperatura em Celsius que deseja converter para Fahrenheit: ')

converter_temp_celsius_usuario_float = float(temp_celsius_usuario)

converter_celsius_para_fahrenheit = float((converter_temp_celsius_usuario_float * 1.8) + 32 )

print(f'A temperatura convertida de Celsius para Fahrenheit é de: {converter_celsius_para_fahrenheit}')