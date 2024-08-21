'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação Python. 
Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, 
indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. 
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. 
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
'''
import copy
verifica = True
contador_de_votos_computados = 0 
lista =  [{'Jogador': 1, 'Votos': 0},{'Jogador': 2, 'Votos': 0},{'Jogador': 3, 'Votos': 0},{'Jogador': 4, 'Votos': 0},{'Jogador': 5, 'Votos': 0},
          {'Jogador': 6, 'Votos': 0},{'Jogador': 7, 'Votos': 0},{'Jogador': 8, 'Votos': 0},{'Jogador': 9, 'Votos': 0},{'Jogador': 10, 'Votos': 0},
          {'Jogador': 11, 'Votos': 0},{'Jogador': 12, 'Votos': 0},{'Jogador': 13, 'Votos': 0},{'Jogador': 14, 'Votos': 0},{'Jogador': 15, 'Votos': 0},
          {'Jogador': 16, 'Votos': 0},{'Jogador': 17, 'Votos': 0},{'Jogador': 18, 'Votos': 0},{'Jogador': 19, 'Votos': 0},{'Jogador': 20, 'Votos': 0},
          {'Jogador': 21, 'Votos': 0},{'Jogador': 22, 'Votos': 0},{'Jogador': 23, 'Votos': 0},
          ]
melhor_jogador = 0
nova_lista = []
nova_lista_organizada = []
while True:

    voto = int(input('Informe um valor entre 1 e 23 ou 0 para sair!'))

    if voto == 0:
        print('Encerrando')
        break
    elif voto > 23:
        print('Não Computado')
        continue
    else:
        print('Computado')
        lista[voto-1]['Votos'] += 1
        contador_de_votos_computados += 1

for idx, dicionario in enumerate(lista):
    if lista[idx]['Votos'] != 0:
        nova_lista.append({'Jogador':lista[idx]['Jogador'],'Votos': lista[idx]['Votos'],'Porcentagem': round((lista[idx]['Votos'] *100) /contador_de_votos_computados)})

nova_lista_organizada= copy.deepcopy(sorted(nova_lista, key=lambda item: item['Votos'], reverse=True))
              
print('Resultado da votação:')
print('Jogador            Votos                %')
for j, valor in enumerate(nova_lista_organizada):
    print(nova_lista_organizada[j]['Jogador'],'                  ', nova_lista_organizada[j]['Votos'],'               ',nova_lista_organizada[j]['Porcentagem'],'%')
print(f'O melhor jogador foi o número {nova_lista_organizada[0]['Jogador']}, com {nova_lista_organizada[0]['Votos']}, correspondendo a {nova_lista_organizada[0]['Porcentagem']}% de total de votos')
