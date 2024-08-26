'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.

input('Digite uma frase:')
'''


vogais = ['a', 'e', 'i', 'o', 'u']
contador_vogal = 0

string_1 = input('Digite uma frase:')

contador_espacos_em_branco = string_1.count(' ')

for letra in string_1:
    for vogal in vogais:
        if letra.upper() == vogal.upper():
            contador_vogal += 1 

print(f'Na string informada existem {contador_espacos_em_branco } espaços em branco.')
print(f'As vogais a, e, i, o, u aparecem {contador_vogal} vezes.')