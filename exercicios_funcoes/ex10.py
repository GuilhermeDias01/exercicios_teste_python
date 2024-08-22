'''
Jogo de Craps. 
Faça um programa que implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''

import random

def joga_dados():
    dados = random.randrange(2,13)
    return(dados)

print('Iniciando o Jogo: ')
print('')

jogada1 = joga_dados()

print(f'Você tirou: {jogada1}')
print('')

if jogada1 == 7 or jogada1 == 11:
    print('O Jogador VENCEU!!')
elif jogada1 == 2 or jogada1 == 3 or jogada1 == 12: 
    print('O Jogador PERDEU!!')
else:
    point = jogada1
    print(f'PONTO!')
    
    while True:
        print('')
        print(f'O valor do ponto é: {point}')
        jogada2 = joga_dados()
        print(f'Você tirou: {jogada2}')
        if jogada2 == 7:
            print('')
            print("Voce tirou um 7 antes de repetir seu ponto, o jogador PERDEU!!")
            break
        elif jogada2 == point: 
            print('')
            print(f'O Jogador VENCEU!!')
            break