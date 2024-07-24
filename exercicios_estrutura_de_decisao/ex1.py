# Faça um Programa que peça dois números e imprima o maior deles.

continua_ou_para = True
while continua_ou_para:
    try:

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
                

        if valor1 > valor2:
            print()
            print('O primeiro valor é maior que o segundo valor.')
        elif valor2 > valor1:
            print()
            print('O segundo valor é maior que o primeiro valor.')
        else:
            print()
            print('Os valores são iguais.')    

    except:
        print('Erro não mapeado')
        
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

