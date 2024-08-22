# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def conta_digitos(n):
    return(str(n[::-1]))

numero = input('Digite o numero: ')

print(conta_digitos(numero))