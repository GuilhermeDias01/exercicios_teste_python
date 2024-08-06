# Faça um Programa que leia três números e mostre o maior deles.

continua_ou_para = True
while continua_ou_para:
    while True:
        try:    
            print()
            valor1 = float(input('Informe o primeiro valor: '))

            if valor1 is not None:
                break
            else:      
                print('Numero incorreto, digite novamente')
        except ValueError as error:
            print()
            print(error)
                
        
    while True:
        try:
            print()
            valor2 = float(input('Informe o segundo valor: '))

            if valor2 is not None:
                break
            else:      
                print('Numero incorreto, digite novamente')    
        except ValueError as error:
            print()
            print(error)

    while True:
        try:
            print()
            valor3 = float(input('Informe o segundo valor: '))

            if valor3 is not None:
                break
            else:      
                print('Numero incorreto, digite novamente')    
        except ValueError as error:
            print()
            print(error)        
                

    if valor1 > valor2 and valor1 > valor3:
        print()
        print('O primeiro valor é o maior.')
    elif valor2 > valor1 and valor2 > valor3:
        print()
        print('O segundo valor é o maior.')
    elif valor3 > valor1 and valor3 > valor2:
        print()
        print('O terceiro valor é o maior.')        
    else:
        print()
        print('Os valores são iguais.')    

    if valor1 < valor2 and valor1 < valor3:
        print()
        print('O primeiro valor é o menor.')
    elif valor2 < valor1 and valor2 < valor3:
        print()
        print('O segundo valor é o menor.')
    elif valor3 < valor1 and valor3 < valor2:
        print()
        print('O terceiro valor é o menor.')        
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