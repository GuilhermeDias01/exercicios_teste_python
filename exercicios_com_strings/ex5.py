'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU

'''

nome = input('Digite seu nome: ')

for i in range(0,len(nome)+1):
    print(nome[0:len(nome)-i:])