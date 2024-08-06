'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

lado1 = float(input('Informe o Primeiro lado do triangulo: ')) 
lado2 = float(input('Informe o Segundo lado do triangulo: '))    
lado3 = float(input('Informe o Terceiro lado do triangulo: '))    



if ((lado1 + lado2) > lado3) and ((lado2 + lado3) > lado1) and ((lado3 + lado1) > lado2):
    print('É um triangulo.')
    if(lado1 == lado2 == lado3):
        print('Triângulo Equilátero')
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3 ):
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')   
else:
    print('Não é um triangulo.')
    