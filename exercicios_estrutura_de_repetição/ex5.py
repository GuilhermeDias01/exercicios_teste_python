# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.
import sys
repete = True

while repete == True:
    populacao_a = int(input('Digite a população do primeiro lugar: '))
    populacao_b = int(input('Digite a população do segundo lugar: '))
    taxa_crescimento_a = float(input('Digite a taxa de crescimento do lugar A: ')) / 100
    taxa_crescimento_b = float(input('Digite a taxa de crescimento do lugar B: ')) / 100
    anos = 0

    if populacao_a < populacao_b and taxa_crescimento_a > taxa_crescimento_b:
        
        while populacao_a <= populacao_b:
            populacao_a += populacao_a * taxa_crescimento_a
            populacao_b += populacao_b * taxa_crescimento_b
            anos += 1

        print(f'A quanidade de anos necessária para a pop A ultrapassar ou igualar a quantidade foi de: {anos} anos')   
        
        valida_repete = input('Deseja realizar a operação novamente? [S]im ou [N]ao').upper()

        if valida_repete == 'S':
            repete = True
        else:
            repete = False

    elif populacao_b < populacao_a and taxa_crescimento_b > taxa_crescimento_a:

        while populacao_b <= populacao_a:
            populacao_a += populacao_a * taxa_crescimento_a
            populacao_b += populacao_b * taxa_crescimento_b
            anos += 1

        print(f'A quanidade de anos necessária para a pop A ultrapassar ou igualar a quantidade foi de: {anos} anos')

        valida_repete = input('Deseja realizar a operação novamente? [S]im ou [N]ao').upper()

        if valida_repete == 'S':
            repete = True
        else:
            repete = False

    else:
        print('Dados inserido de forma errada.')
        print(f'Para comparar a populacao A com a populacao B a quntidade da {populacao_a=} deve ser menor que a {populacao_b=} e a {taxa_crescimento_a=} deve ser maior que a {taxa_crescimento_b=}.')
        print('OU.')
        print(f'Para comparar a populacao B com a populacao A a quntidade da {populacao_b=} deve ser menor que a {populacao_a=} e a {taxa_crescimento_b=} deve ser maior que a {taxa_crescimento_a=}.')
        print('OU.')
        print('Contém dados iguais.')

        valida_repete = input('Deseja realizar a operação novamente? [S]im ou [N]ao').upper()

        if valida_repete == 'S':
            repete = True
        else:
            repete = False