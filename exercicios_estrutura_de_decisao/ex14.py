'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota_usuario1 = float(input('Informe a primeira nota: '))
nota_usuario2 = float(input('Informe a segunda nota: '))

media = (nota_usuario1 + nota_usuario2) / 2
conceito = ''


if media >= 9:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
elif media >= 0:
    conceito = 'E'
else:
    print('Média Inválida')

print(f'Nota 1: {nota_usuario1} e Nota 2: {nota_usuario2}')
print(f'Média: {media:.2f}')
print(f'Conceito: {conceito}')
if conceito == 'A' or conceito == 'B' or conceito =='C':
    print('Aprovado')
else:
    print('Reprovado')


