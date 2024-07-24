# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

import string

vogais = 'a', 'e', 'i', 'o', 'u',
continua_ou_para = True

while continua_ou_para:
    try:
        while True:
            try:    
                print()
                letra_digitada = input('Informe a letra: ')

                if letra_digitada.isdigit():
                    print('Você digito um número, por favor informe a letra.')
                    continue
                elif len(letra_digitada) > 1:
                    print("Você digitou mais de uma letra.")
                    continue
                elif letra_digitada in string.punctuation:
                    print("Você digitou um caractere especial.")
                    continue
                                
                if letra_digitada in vogais:                    
                    print(f'A letra "{letra_digitada.lower()}" é uma vogal')
                else:
                    print(f'A letra "{letra_digitada.lower()}" é uma consoante')
            except (Exception) as error:
                print()
                print(error)
                
    except (Exception) as error:
        print()
        print(error)

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

