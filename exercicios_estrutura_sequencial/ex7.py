# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_valor_informado_usuario = input('Informe o valor de um dos lados do quadrado: ')

lado_valor_informado_usuario_float = float(lado_valor_informado_usuario)

valor_area_quadrado = lado_valor_informado_usuario_float**2

valor_area_quadradovalor_area_quadrado = valor_area_quadrado * 2

print(f'O dobro da area para o lado informado é: {valor_area_quadradovalor_area_quadrado:.2f}')