# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

valor_altura_usuário = input('Digite a sua altura: ')

altura_usuario_float = float(valor_altura_usuário)

peso_ideal_homem = (72.7 * altura_usuario_float ) - 58
peso_ideal_mulher = (62.1 * altura_usuario_float ) - 44.7

print(f'Em caso de homem o peso ideal para essa altura seria de: {peso_ideal_homem:.2f}')
print(f'Em caso de mulher o peso ideal para essa altura seria de: {peso_ideal_mulher:.2f}')