# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

import math

usuario_raio_valor = input('Digite o valor do raio do circulo: ')

usuario_raio_valor_float = float(usuario_raio_valor)

valor_da_area_circulo = math.pi * (usuario_raio_valor_float**2)

print(f'O valor da área do circulo é de: {valor_da_area_circulo:.2f}')