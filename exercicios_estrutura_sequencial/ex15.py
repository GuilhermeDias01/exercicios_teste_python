'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

horas_trabalhas = input('Digite quantas horas trabalha por mês: ')
dinheiro_por_hora = input('Digite qual é o valor da hora trabalhada: ')

salario_bruto_float = float(horas_trabalhas) * float(dinheiro_por_hora)

valor_ir = (salario_bruto_float * 1.11) - salario_bruto_float  
valor_inss = (salario_bruto_float * 1.08) - salario_bruto_float 
valor_sindicado = (salario_bruto_float * 1.05) - salario_bruto_float 
tupla_de_valores = valor_ir, valor_inss, valor_sindicado,
valor_liquido = (salario_bruto_float) - sum(tupla_de_valores)

print(f'+ Salario Bruto: R$ {salario_bruto_float:.2f}')
print(f'- IR (11%): R$ {valor_ir:.2f}') 
print(f'- INSS (8%): R$ {valor_inss:.2f}')
print(f'- Sindicato (5%): R$ {valor_sindicado:.2f}')
print(f'= Salário Liquido: R$ {valor_liquido:.2f}')

