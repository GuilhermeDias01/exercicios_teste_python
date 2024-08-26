'''
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não
'''

string_1 = input('Digite o conteúdo da string 1: ')

string_1_sem_espaco = string_1.replace(' ', '').lower()

string_2_sem_espaco_invertida = string_1_sem_espaco[::-1]

if string_1_sem_espaco == string_2_sem_espaco_invertida:
    print(f'A palvra ou frase "{string_1}" é um palíndromo.')
else:
    print(f'A palvra ou frase "{string_1}" NÃO é um palíndromo.')

