#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

entrada_usuario = input('Digite o periodo que você estuda, sendo; M-matutino ou V-Vespertino ou N- Noturno:').upper()

if entrada_usuario == 'M':
    print('Bom dia')
elif entrada_usuario == 'V':
    print('Boa Tarde')    
elif entrada_usuario == 'N':
    print('Boa noite')
else:
    print('Valor Inválido!')
