#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

n = int(input('Digite o numero: '))
count = 0
lista_numeros = []

for i in range(n):
    contador = (i+1)
    if n % contador == 0:
        lista_numeros.append(contador)
        count += 1


if count == 2:
    print('O número é primo.')
else:
    print('O número não é primo. Pois ele é divisivel pelos números abaixo:')
    print(lista_numeros)
