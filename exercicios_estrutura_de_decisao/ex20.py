'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

nota1 = float(input('Informe o valor da pimeira nota: '))
nota2 = float(input('Informe o valor da segunda nota: '))
nota3 = float(input('Informe o valor da terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'Sua média foi de: {media}')

if media >= 7 and media <= 9.99:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção.')
else:
    print('Reprovado.')