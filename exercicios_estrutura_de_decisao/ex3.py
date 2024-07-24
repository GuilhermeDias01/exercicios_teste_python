# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, 
# M - Masculino, 
# Sexo Inválido.

continua_ou_para = True

while continua_ou_para:
    try:
        print()
        
        # Loop interno para garantir uma entrada de sexo válida
        while True:
            sexo = input('Informe o sexo, [M] para masculino e [F] para feminino: ')
            
            if str.lower(sexo) == 'm':
                print('O sexo informado é Masculino.')
                break  # Sai do loop interno se a entrada for válida
            elif str.lower(sexo) == 'f':
                print('O sexo informado é Feminino.')
                break  # Sai do loop interno se a entrada for válida
            else:
                print('Sexo inválido. Por favor, informe [M] para Masculino ou [F] para Feminino.')

    except ValueError as error:
        print(error)
        print('Erro ao processar o sexo.')

    print()
    
    # Loop para garantir uma entrada válida para continuar ou sair
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
