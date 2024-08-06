'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

import string

continua_ou_para = True

while continua_ou_para:
    
    while True:
        try:    
            print()
            nota1 = float(input('Informe o valor da primeira nota: '))

            if nota1 is not None:
                break
            else:      
                print('Numero incorreto, digite novamente')
        except ValueError as error:
            print()
            print(error)
                
        
    while True:
        try:
            print()
            nota2 = float(input('Informe o valor da segunda nota: '))

            if nota2 is not None:
                break
            else:      
                print('Numero incorreto, digite novamente')    
        except ValueError as error:
            print()
            print(error)
                
    media_notas =  (nota1 + nota2) / 2  

    if media_notas >= 7 and media_notas <= 9.9:
            print()
            print('Aprovado.')
    elif media_notas == 10:
            print()
            print('Aprovado com Distinção.')
    elif media_notas > 10:
            print()
            print(f'A média {media_notas} informada não é valida.')
    else:
            print()
            print('Reprovado.')     
                
    

    print()
    while True:
        
        continua_ou_para = input('Para continuar digite [C] ou [S] para sair: ').strip().lower()
        
        if continua_ou_para == 'c':
            break  
        elif continua_ou_para == 's':
            continua_ou_para = False  
            print('Saindo do programa.')
            break
        else:
            print('Opção inválida. Por favor, digite [C] para continuar ou [S] para sair.')