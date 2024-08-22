'''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''

lista_de_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
  
def chama_nova_data(data):
    data = data.replace('/', '')
    idx = int(data[2:4])
    return(print(f'{str(data[0:2])} de {lista_de_mes[idx-1]} de {str(data[4:8])}'))

data = input('Digite a data: ')

chama_nova_data(data)


