'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Informe um nome: ')
while len(nome) <= 3:
    nome = input('Nome incorreto, tente novamente: ')

idade = int(input('Informe sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade incorreta, tente novamente: '))

salario = float(input('Informe seu salário: '))
while salario < 0:
    salario = float(input('Salário incorreto, tente novamente: '))

sexo = input('Informe o sexo, [F] ou [M]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Sexo incorreto, tente novamente: ').upper()

estado_civil = input('Informe o estado civil, [S], [C], [V] ou [D]: ').upper()
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = input('Estado Civil incorreto, tente novamente: ').upper()