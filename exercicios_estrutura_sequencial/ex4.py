# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeira_nota = input('Informe a primeira nota: ')
segunda_nota = input('Informe a segunda nota: ')
terceira_nota = input('Informe a terceira nota: ')
quarta_nota = input('Informe a quarta nota: ')


primeira_nota_float = float(primeira_nota)
segunda_nota_float = float(segunda_nota)
terceira_nota_float = float(terceira_nota)
quarta_nota_float = float(quarta_nota)

media_notas = (primeira_nota_float + segunda_nota_float + terceira_nota_float+ quarta_nota_float) / 4

print(f'A média das notas é: {media_notas}')