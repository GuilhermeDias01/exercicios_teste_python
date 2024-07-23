# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

valor_altura_usuário = input('Digite a sua altura: ')

altura_usuario_float = float(valor_altura_usuário)

peso_ideal = (72.7 * altura_usuario_float ) - 58

print(f'O peso ideal para sua altura é de: {peso_ideal:.2f}')