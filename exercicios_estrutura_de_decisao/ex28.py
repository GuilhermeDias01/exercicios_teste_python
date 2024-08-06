'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

tipo_de_carne = input('informe o tipo de carne [F]ile duplo, [A]lcatra e [P]icanha: ').upper()
quantidade = int(input('Digite a quntiadade em KG desejada: '))

if tipo_de_carne == 'F' and quantidade <= 5:
    valor_a_pagar = quantidade * 4.90
    tipo_de_carne_escolhida = 'File Duplo'
elif tipo_de_carne == 'F' and quantidade > 5:
    valor_a_pagar = quantidade * 5.80
    tipo_de_carne_escolhida = 'File Duplo'    
elif tipo_de_carne == 'A' and quantidade <= 5:
    valor_a_pagar = quantidade * 5.90
    tipo_de_carne_escolhida = 'Alcatra'
elif tipo_de_carne == 'A' and quantidade > 5:
    valor_a_pagar = quantidade * 6.80
    tipo_de_carne_escolhida = 'Alcatra'
elif tipo_de_carne == 'P' and quantidade <= 5:
    valor_a_pagar = quantidade * 6.90
    tipo_de_carne_escolhida = 'Picanha'
elif tipo_de_carne == 'P' and quantidade > 5:
    valor_a_pagar = quantidade * 7.80
    tipo_de_carne_escolhida = 'Picanha'
else:
    print('Opção Incorreta')

forma_de_pag = input('A compra será feita com o cartão da loja? [S]im  ou [N]ão.').upper()

if forma_de_pag == 'S':
    desconto = valor_a_pagar * 0.05
    valor_total_a_pagar = valor_a_pagar - desconto
    forma_de_pag2 = 'Cartão da Loja'
    print(f'O tipo de carne selecionada foi {tipo_de_carne_escolhida}, a quantidade escolhida foi de {quantidade}KG, o preço total foi de R${valor_a_pagar:.2f}, o tipo de pagamento selecionado foi {forma_de_pag2}, o valor de desconto foi de {desconto:.2f} e o valor total a ser pago é de R$ {valor_total_a_pagar}. ')
else:
    valor_total_a_pagar = valor_a_pagar
    forma_de_pag = 'Outros'
    desconto = 0
    print(f'O tipo de carne selecionada foi {tipo_de_carne_escolhida}, a quantidade escolhida foi de {quantidade}KG, o preço total foi de R${valor_a_pagar:.2f} e o tipo de pagamento selecionado foi {forma_de_pag}.' )