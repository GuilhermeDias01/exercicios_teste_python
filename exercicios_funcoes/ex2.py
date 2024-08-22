'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

'''

def imprime_sequencia_numero(n):
    for i in range(1,n+1):
        print(i , end='\n')
        if i == n:
            break
        else:
            for j in range(1,n+1):
                if i >= j:
                    print(j, end='')


imprime_sequencia_numero(5)