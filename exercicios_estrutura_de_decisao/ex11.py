'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario_colaborador = float(input('Informe o salário: '))
percentual_utilziado = 0

if salario_colaborador <= 280.00:
    novo_salario = salario_colaborador * 1.20
    percentual_utilziado = '20%'
elif salario_colaborador > 280.00  and salario_colaborador < 700.00:
    novo_salario = salario_colaborador * 1.15
    percentual_utilziado = '15%'
elif salario_colaborador >= 700.00  and salario_colaborador < 1500.00:
    novo_salario = salario_colaborador * 1.10
    percentual_utilziado = '10%'
else:
    novo_salario = salario_colaborador * 1.05
    percentual_utilziado = '5%'

print()
print(f'O salário antes do reajuste: {salario_colaborador:.2f}')
print(f'O percentual de aumento aplicado: {percentual_utilziado}')
print(f'O valor do aumento: {(novo_salario-salario_colaborador):.2f}')
print(f'O novo salário, após o aumento: {novo_salario:.2f}')