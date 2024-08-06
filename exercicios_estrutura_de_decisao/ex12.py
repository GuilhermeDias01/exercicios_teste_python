'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
''' 
horas_trabalhas = input('Digite quantas horas trabalha por mês: ')
dinheiro_por_hora = input('Digite qual é o valor da hora trabalhada: ')

salario_bruto_float = float(horas_trabalhas) * float(dinheiro_por_hora)
porcentagem_desconto = 0

if salario_bruto_float <= 900.00:
    valor_ir = 0 
    porcentagem_desconto = 'ISENTO'
elif salario_bruto_float > 900.00 and salario_bruto_float <= 1500.00:
    valor_ir = (salario_bruto_float * 1.05) - salario_bruto_float
    porcentagem_desconto = '5%'   
elif salario_bruto_float > 1500.00 and salario_bruto_float <= 2500.00:
    valor_ir = (salario_bruto_float * 1.10) - salario_bruto_float  
    porcentagem_desconto = '10%'  
else:
    valor_ir = (salario_bruto_float * 1.20) - salario_bruto_float 
    porcentagem_desconto = '20%'  

valor_inss = (salario_bruto_float * 1.10) - salario_bruto_float 
valor_FGTS = (salario_bruto_float * 1.11) - salario_bruto_float 
total_descontos = valor_ir + valor_inss
salario_liquido = salario_bruto_float - total_descontos

print(f'+ Salario Bruto: R$ {salario_bruto_float:.2f}')
print(f'- IR {porcentagem_desconto}: R$ {valor_ir:.2f}') 
print(f'- INSS (10%): R$ {valor_inss:.2f}')
print(f'  FGTS (11%): R$ {valor_FGTS:.2f}')
print(f'  Total de descontos: R$ {total_descontos:.2f}')
print(f'= Salário Liquido: R$ {salario_liquido:.2f}')

