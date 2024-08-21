'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:

1- necessita da esfera;
2- necessita de limpeza; 
3- necessita troca do cabo ou conector; 
4- quebrado ou inutilizado 

Uma identificação igual a zero encerra o programa. 

Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''
import random

qntd_mouses = 100
lista_de_mouses = []
cod_esfera = 0 
cod_limpeza = 0
cod_troca = 0
cod_quebrado = 0

for i in range(0,qntd_mouses):
    codigo_mouse = random.randrange(6283752560,9283752560)
    codigo_status = random.randrange(1,5)
    dicionario = {'Código do Mouse': codigo_mouse, 'Código do Status': codigo_status}
    lista_de_mouses.append(dicionario)

for lista in lista_de_mouses:
    if lista['Código do Status'] == 1:
        cod_esfera += 1
    elif lista['Código do Status'] == 2:
        cod_limpeza += 1
    elif lista['Código do Status'] == 3:
        cod_troca += 1
    else:
        cod_quebrado += 1

print('Situação                        Quantidade              Percentual')
print(f'1- Necessita da esfera                 {cod_esfera}               {(cod_esfera*100)/qntd_mouses}%')
print(f'2- Necessita de limpeza                {cod_limpeza}               {(cod_limpeza*100)/qntd_mouses}%')
print(f'3- Necessita troca do cabo ou conector {cod_troca}               {(cod_troca*100)/qntd_mouses}%')
print(f'4- Quebrado ou inutilizado             {cod_quebrado}               {(cod_quebrado*100)/qntd_mouses}%')
