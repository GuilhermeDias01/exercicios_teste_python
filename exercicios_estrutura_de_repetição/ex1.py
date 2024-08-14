# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = True

while nota == True:

    nota_usuario = float(input('Informe uma nota entre 0 e 10: '))

    if nota_usuario >= 0 and nota_usuario <= 10:
        print('')
        print(f'A nota {nota_usuario:.2f} é uma nota válida')
        nota = False
    else:
        print('')
        print(f'A nota {nota_usuario:.2f} é uma nota inválida. Tente novamente!')



#exemplo 2:

nota=float(input("informe um numero de 0 a 10: "))

while (nota>10) or (nota<0):
    nota=float(input("informe um numero de 0 a 10: "))