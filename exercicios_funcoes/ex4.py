# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


def verifica_numero(n):
    if n > 0:
        verifica = 'P'
    else:
        verifica = 'N'
    return(verifica)

print(verifica_numero(0))