'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

tipo_combustivel = input('Deseja abastecer com [A]-álcool ou [G]-gasolina: ').upper()
quantidade_litros = int(input('Digite a quantiadade que deseja abastecer: '))

if tipo_combustivel == 'A' and quantidade_litros <= 20:
    desconto = (quantidade_litros * 1.90) * 0.03
    total_a_pagar = (quantidade_litros * 1.90) - desconto
elif tipo_combustivel == 'A' and quantidade_litros > 20:
    desconto = (quantidade_litros * 1.90) * 0.05
    total_a_pagar = (quantidade_litros * 1.90) - desconto
elif tipo_combustivel == 'G' and quantidade_litros <= 20:
    desconto = (quantidade_litros * 2.50) * 0.04
    total_a_pagar = (quantidade_litros * 2.50) - desconto
else:
    desconto = (quantidade_litros * 2.50) * 0.06
    total_a_pagar = (quantidade_litros * 2.50) - desconto

print(f'O valor total a ser pago é de: R${total_a_pagar:.2f}')