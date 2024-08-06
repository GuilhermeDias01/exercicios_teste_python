# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

entrada_usuario = int(input('Informe o dia correspondente ao dia da semana: '))

if entrada_usuario == 1:
    print('Domingo')
elif entrada_usuario == 2:
    print('Segunda-Feira')
elif entrada_usuario == 3:
    print('Terça-Feira')
elif entrada_usuario == 4:
    print('Quarta-Feira')
elif entrada_usuario == 5:
    print('Quinta-Feira')
elif entrada_usuario == 6:
    print('Sexta-Feira')
elif entrada_usuario == 7:
    print('Sábado')
else:
    print('Entrada Inválida.')   
