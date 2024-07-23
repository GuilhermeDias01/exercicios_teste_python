'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
considere latas cheias.
'''

tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = tamanho / 6.0
latas18 = int(litros / 18.0)
latas3_6 = int(litros / 3.6)
#latas
if litros % 18 != 0:
    latas18 += 1
print(f'Utilizando latas de 18 Litros você deverá comprar {latas18} latas, e o total será de R$ {latas18 * 80}')
#galões
if litros % 3.6 != 0:
    latas3_6 += 1

print(f'Utilizando latas de 3.6 Litros você deverá comprar {latas3_6} latas, e o total será de R$ {latas3_6 * 25}')

#Misutra de latas e galões
litros_mais_porcentagem = round(litros * 1.10)
qntd_latas = int(litros_mais_porcentagem / 18)
qntd_galoes = int((litros_mais_porcentagem - (qntd_latas * 18)) / 3.6)

if litros_mais_porcentagem - (qntd_latas * 18) % 3.6 != 0:
    qntd_galoes += 1

total_gasto = (qntd_latas * 80) + (qntd_galoes * 25)
    

print(f'Você deverá comprar {qntd_latas} latas de 18L e {qntd_galoes} galões de 3,6L o valor total gasto será de R$ {total_gasto:.2f}')



