# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, 
# M - Masculino, 
# Sexo Inválido.

continua_ou_para = True

while continua_ou_para:
    try:
        print()
                
        while True:
            sexo = input('Informe o sexo, [M] para masculino e [F] para feminino: ')
            
            if str.lower(sexo) == 'm':
                print('O sexo informado é Masculino.')
                break  
            elif str.lower(sexo) == 'f':
                print('O sexo informado é Feminino.')
                break  #
            else:
                print('Sexo inválido. Por favor, informe [M] para Masculino ou [F] para Feminino.')

    except ValueError as error:
        print(error)
        print('Erro ao processar o sexo.')

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
