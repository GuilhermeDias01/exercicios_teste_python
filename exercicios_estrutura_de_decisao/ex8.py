# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

continua_ou_para = True
while continua_ou_para:
    while True:
        try:    
            print()
            produto1 = float(input('Informe o valor do primeiro produto: '))

            if produto1 is not None:
                break
            else:      
                print('Valor incorreto, digite novamente')
        except ValueError as error:
            print()
            print(error)
                
        
    while True:
        try:
            print()
            produto2 = float(input('Informe o valor do segundo produto: '))

            if produto2 is not None:
                break
            else:      
                print('Valor incorreto, digite novamente')    
        except ValueError as error:
            print()
            print(error)

    while True:
        try:
            print()
            produto3 = float(input('Informe o valor do terceiro produto: '))

            if produto3 is not None:
                break
            else:      
                print('Valor incorreto, digite novamente')    
        except ValueError as error:
            print()
            print(error)        
                
    
    
    if produto1 < produto2 and produto1 < produto3:
        print()
        print('O produto recomendo a ser comprando é o primeiro.')
    elif produto2 < produto1 and produto2 < produto3:
        print()
        print('O produto recomendo a ser comprando é o segundo.')
    elif produto3 < produto1 and produto3 < produto2:
        print()
        print('O produto recomendo a ser comprando é o terceiro.')       
    else:
        print()
        print('Os valores são iguais.')    

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