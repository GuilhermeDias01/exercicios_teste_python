'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

numero_usuario = input('Digite um numero inteiro de 0 a 999: ')
numero_usuario_int = int(numero_usuario)
medida_unidade = ''
medida_dezena = ''
medida_centena = ''
separador1 = 'e'
separador2 = ','

if numero_usuario_int == 0 or numero_usuario_int <= 9:
    unidade =  int(numero_usuario[0])
    
    if unidade == 0 or unidade == 1:
        medida_unidade = 'unidade'
    elif unidade >= 2 or unidade <= 9:
        medida_unidade = 'unidades'
    
    print(f'{unidade} {medida_unidade}')

elif numero_usuario_int >= 10 and numero_usuario_int <= 99:
    unidade =  int(numero_usuario[1])
    dezena =  int(numero_usuario[0])

    if unidade == 0 or unidade == 1:
        medida_unidade = 'unidade'
    elif unidade >= 2 or unidade <= 9:
        medida_unidade = 'unidades'

    if dezena == 0 or dezena == 1:
        medida_dezena = 'dezena'
    elif dezena >= 2 or dezena <= 9:
        medida_dezena = 'dezenas'

    print(f'{dezena} {medida_dezena} {separador1} {unidade} {medida_unidade}')

else:
    unidade =  int(numero_usuario[2])
    dezena =  int(numero_usuario[1])
    centena =  int(numero_usuario[0])

    if unidade == 0 or unidade == 1:
        medida_unidade = 'unidade'
    elif unidade >= 2 or unidade <= 9:
        medida_unidade = 'unidades'

    if dezena == 0 or dezena == 1:
        medida_dezena = 'dezena'
    elif dezena >= 2 or dezena <= 9:
        medida_dezena = 'dezenas'

    if centena == 1 or centena == 0:
        medida_centena = 'centena'
    elif centena >= 2 or centena <= 9:
        medida_centena = 'centenas'
    
    print(f'{centena} {medida_centena} {separador2} {dezena} {medida_dezena} {separador1} {unidade} {medida_unidade}')    


    







