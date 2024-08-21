'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 

Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
'''
import random

lista_de_salarios = []
lista_de_abono = []
contador_de_colaboradores = 0
contador_de_valor_minimo = 0
verificador = 0
qntd_colaboradores = 50

while verificador < qntd_colaboradores:

    salario = random.randrange(100, 12000)

    if salario == 0:
        break

    if salario * 0.20 < 100:
        lista_de_salarios.append(salario)
        lista_de_abono.append(100)
        contador_de_colaboradores += 1
        contador_de_valor_minimo += 1
        verificador += 1
    else:
        lista_de_salarios.append(salario)
        lista_de_abono.append(salario * 0.20)
        contador_de_colaboradores += 1
        verificador += 1

maior_valor_pago = 0
for i,valor in enumerate(lista_de_abono):
    if lista_de_abono[i] > maior_valor_pago:
        maior_valor_pago = valor
    else:
        maior_valor_pago = maior_valor_pago   

print('Projeção de Gastos com Abono')
print('============================')
print('')
for salario in lista_de_salarios:
    print(f'Salario: {salario:.2f}')
print('')
print('Salário    - Abono  ')
for i,salario in enumerate(lista_de_salarios):
    print(f'R$ {lista_de_salarios[i]:.2f} - R$ {lista_de_abono[i]:.2f}')
print('')
print(f'Foram processados {contador_de_colaboradores} colaboradores.')
print(f'Total gasto com abonos: R$ {sum(lista_de_abono):.2f}')
print(f'Valor mínimo pago a {contador_de_valor_minimo} colaboradores')
print(f'Maior valor de abono pago: R$ {maior_valor_pago:.2f}')
