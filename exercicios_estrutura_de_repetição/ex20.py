# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
while True:

    n = int(input('Digite o numero: '))

    if n > 0 and n < 16:
        resultado = 1

        for i in range(1, n + 1):
            resultado *= i
            
        print(f'{resultado= }')
        
    else:
        print('')
        print('Numero não permitido')

    print('')

    tentar_novamente = input('Deseja tentar novamente [S]im ou [N]ão:  ')

    print('')

    if tentar_novamente.upper() == 'S':
        continue
    else:
        break