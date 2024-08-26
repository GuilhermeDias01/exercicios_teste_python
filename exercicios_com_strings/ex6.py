'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''

lista_de_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data_nascimento = input('Digite a data no formato (dd/mm/aaaa): ')  

idx = int(data_nascimento[3:5])

print(f'Você nasceu em {data_nascimento[0:2:]} de {lista_de_mes[idx-1]} de {data_nascimento[6:10:]}')

