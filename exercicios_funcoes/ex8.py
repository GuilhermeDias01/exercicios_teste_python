# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.


def conta_digitos(n):
    contador = 0
    for i in n:
        contador += 1
    return(contador)

numero = input('Digite o numero: ')

print(conta_digitos(numero))