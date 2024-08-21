'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outros                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''
import random
import copy

lista_sistemaop_votos_porcent = [{'Sistema Operacional': 'Windows', 'Votos': 0, 'Porcentagem': 0},{'Sistema Operacional': 'Unix', 'Votos': 0, 'Porcentagem': 0},
                               {'Sistema Operacional': 'Linux', 'Votos': 0, 'Porcentagem': 0},{'Sistema Operacional': 'Netware', 'Votos': 0, 'Porcentagem': 0},
                               {'Sistema Operacional': 'Mac OS', 'Votos': 0, 'Porcentagem': 0},{'Sistema Operacional': 'Outros', 'Votos': 0, 'Porcentagem': 0},]

contador_de_votos_computados = 0

while True:
    for i in range (1,8801):
        voto = random.randrange(1, 7)
        if voto == 0:
            break
        elif voto > 6:
            continue
        else:
            lista_sistemaop_votos_porcent[voto-1]['Votos'] += 1
            contador_de_votos_computados += 1
    break   

for idx, dicionario in enumerate(lista_sistemaop_votos_porcent):
    if lista_sistemaop_votos_porcent[idx]['Votos'] != 0:
        lista_sistemaop_votos_porcent[idx]['Porcentagem'] = round((lista_sistemaop_votos_porcent[idx]['Votos'] *100) /contador_de_votos_computados)

mais_votado = copy.deepcopy(lista_sistemaop_votos_porcent[0])

for i in range (0,5):
    if i <= 4:
        if mais_votado['Votos'] > lista_sistemaop_votos_porcent[i+1]['Votos']:
            ...
        else:
            mais_votado = copy.deepcopy(lista_sistemaop_votos_porcent[i+1])   
      
print(mais_votado)

print('Sistema Operacional     Votos    %')
print('-------------------     -----   ---')
for idx, valor in enumerate(lista_sistemaop_votos_porcent):
    print(f'{lista_sistemaop_votos_porcent[idx]['Sistema Operacional']}                 {lista_sistemaop_votos_porcent[idx]['Votos']}       {lista_sistemaop_votos_porcent[idx]['Porcentagem']}%')
print('-------------------     -----')    
print(f'Total                    {contador_de_votos_computados}')   
print(f'O Sistema Operacional mais votado foi o {mais_votado['Sistema Operacional']}, com {mais_votado['Votos']} votos, correspondendo a {mais_votado['Porcentagem']}% dos votos.')