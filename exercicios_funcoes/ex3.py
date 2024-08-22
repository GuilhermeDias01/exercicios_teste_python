# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_3_numeros(n1,n2,n3):
    soma = n1 + n2 + n3
    return(soma)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

print(soma_3_numeros(n1,n2,n3))