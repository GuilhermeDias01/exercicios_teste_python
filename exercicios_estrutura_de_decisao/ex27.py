'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

quantidade_maca = int(input('Digite a quntiadade em KG desejada para Maças: '))
quantidade_morango = int(input('Digite a quntiadade em KG desejada para Morango: '))

if quantidade_maca <= 5:
    valor_total_maca = quantidade_maca * 1.80
else:
    valor_total_maca = quantidade_maca * 1.50

if quantidade_morango <= 5:
    valor_total_morango = quantidade_morango * 2.50
else:
    valor_total_morango = quantidade_morango * 2.20

if (valor_total_maca + valor_total_morango) > 25 or (quantidade_morango + quantidade_maca) > 8:
    desconto = (valor_total_maca + valor_total_morango) * 0.10
    valor_total_a_pagar = (valor_total_maca + valor_total_morango) - desconto
else:
    valor_total_a_pagar = valor_total_maca + valor_total_morango


print(f'O valor a ser pago pelo cliente é de: R${valor_total_a_pagar}')