# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_por_horas = input('Digite o valor recebido em real por cada hora trabalhada: ')

salario_por_horas_float = float(salario_por_horas)

horas_trabalhadas_mes = input('Digite o quantas horas você trabalha por mês: ')

horas_trabalhadas_mes_int = int(horas_trabalhadas_mes)

valor_total_salario_mes = salario_por_horas_float * horas_trabalhadas_mes_int

print(f'O valor total recebido por mês é: {valor_total_salario_mes:.2f}')