'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''


base = int(input('Informe a base: '))
expoente = int(input('Informe o exponente: '))
resultado = 1

for i in range(expoente):
    resultado *= base
    
print(resultado)



