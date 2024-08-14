# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

if numero1 < numero2:

    for numeros in range(numero1 + 1, numero2):
        print(numeros)

else:
    
    for numeros in range(numero2 + 1 , numero1):
        print(numeros)