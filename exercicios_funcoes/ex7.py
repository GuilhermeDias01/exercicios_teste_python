'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(valor_prestacao, dias_em_atraso):
    valor = valor_prestacao + (valor_prestacao * 0.03) + ((valor_prestacao * 0.01) * dias_em_atraso)
    return(valor)

lista_de_valores = []

while True:

    valor_prestacao = float(input("Informe o valor da prestacao "))

    if valor_prestacao == 0:
        print('O programa está sendo encerrado.')
        print('')
        break

    dias_em_atraso = int(input("Informe quantos dias essas prestacao está em atraso: "))

    if dias_em_atraso > 0:
        print(f'Valor a ser pago: R$ {valorPagamento(valor_prestacao,dias_em_atraso)}')
        lista_de_valores.append(valorPagamento(valor_prestacao,dias_em_atraso))
    else:
        print(f'Valor a ser pago: R$ {valor_prestacao}')
        lista_de_valores.append(valor_prestacao)

print('Relatório:')       
print(f'A quantidade de prestações é de {len(lista_de_valores)} e a soma do valor das prestações é de: R$ {sum(lista_de_valores)}')