'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''

lista_de_veiculos = []
lista_de_consumo_de_combustivel_por_veiculo = []
verificador = 0
qntd_colaboradores = 5

while verificador < qntd_colaboradores:

    veiculo = input('Informe o nome do modelo do carro: ')
    consumo_de_combustivel_do_veiculo = float(input('Informe a quantidade de KM que ele percorre com 1 Litro de gasolina: '))

    lista_de_veiculos.append(veiculo)
    lista_de_consumo_de_combustivel_por_veiculo.append(consumo_de_combustivel_do_veiculo)
    verificador += 1

for i, veiculo in enumerate(lista_de_veiculos):
    print(f'Veiculo {i+1}')
    print(f'Nome: {veiculo}')
    print(f'Km por litro: {lista_de_consumo_de_combustivel_por_veiculo[i]:.1f}') 

menor_consumo = 0

for i,valor in enumerate(lista_de_consumo_de_combustivel_por_veiculo):
    if lista_de_consumo_de_combustivel_por_veiculo[i] > menor_consumo:
        menor_consumo = valor
        carro_menor_consumo = lista_de_veiculos[i]
        
print('')
print('Relatório Final')
for i, veiculo in enumerate(lista_de_veiculos):
    print(f'{i+1} - {veiculo}           -   {lista_de_consumo_de_combustivel_por_veiculo[i]:.1f} - {1000/lista_de_consumo_de_combustivel_por_veiculo[i]:.1f} litros - R$ {(1000/lista_de_consumo_de_combustivel_por_veiculo[i]) * 2.25:.2f}')
print('')
print(f'O menor consumo é do {carro_menor_consumo}.')