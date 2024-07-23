#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

informa_temperatura_fahrenheit_usuario = input('Informe em números a temperatura atual em Fahrenheit que deseja converter para Celsius: ')

informa_temperatura_fahrenheit_usuario_float = float(informa_temperatura_fahrenheit_usuario)

conversor_de_temp_fahren_p_celsius_float = float((informa_temperatura_fahrenheit_usuario_float - 32) / 1.8)

print(f'A temperatura convertida em Celsius é: {conversor_de_temp_fahren_p_celsius_float:.2f}')