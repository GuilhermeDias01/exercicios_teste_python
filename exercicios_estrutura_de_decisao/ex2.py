# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


continua_ou_para = True

while continua_ou_para:
    try:
        print()
        
        while True:
            valor = float(input('Informe o valor: '))
            
            if valor > 0:
                print('O valor informado é Positivo.')
                break  
            elif valor < 0:
                print('O valor informado é Negativo.')
                break 
            elif valor == 0:
                print('O valor informado é igual a 0')
                break 
            
    except ValueError as error:
        print(error)
        print('Erro ao processar o valor.')

    print()
    
    while True:
        
        continua_ou_para = input('Para continuar digite [C] ou [S] para sair: ').strip().lower()
        
        if continua_ou_para == 'c':
            break  # Sai do loop de opções e reinicia o ciclo
        elif continua_ou_para == 's':
            continua_ou_para = False  # Para o loop principal
            print('Saindo do programa.')
            break
        else:
            print('Opção inválida. Por favor, digite [C] para continuar ou [S] para sair.')