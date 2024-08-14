# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

laco1 = True

while laco1 == True:

    usuario = input('Informe seu usuário: ')
    senha = input('Informe sua senha: ')

    if usuario == senha:
        print('')
        print(f'O usuário "{usuario}" é igual a senha digitada, escolha outra senha')
        laco2 = True
        while laco2 == True:
            print('')
            senha = input('Informe sua senha: ')
            if usuario == senha:
                print('')
                print(f'O usuário "{usuario}" é igual a senha digitada, escolha outra senha')
            else:
                print('')
                print('Senha Válida') 
                laco2 = False 
                laco1 = False
    else:
        print('')
        print(f'O usuário e senha são válidos.')
        laco1 = False


# exemplo 2:

print("faça já seu cadastro:")
usuario=str(input("usuário--> "))
senha=str(input("senha-->"))

while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("usuário--> "))
	senha=str(input("senha-->"))
else:
	print("cadastrado efetuado com sucesso")