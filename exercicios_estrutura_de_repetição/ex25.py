# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, 
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

qntd_pessoas = int(input('informe a quantidade de pessoas: '))
count = 1
total_idades = 0

while count < (qntd_pessoas + 1):

    idade = int(input(f'Informe a indade da pessoa Nº {count}: '))
    total_idades += idade

    count += 1

media = total_idades /qntd_pessoas

if media >= 0 and media <= 25:
    print(f'A média de idade é de: {media}')
    print('O grupo é considerado JOVEM')
elif media >= 26 and media <= 60:
    print(f'A média de idade é de: {media}')
    print('O grupo é considerado ADULTO')
else:
    print(f'A média de idade é de: {media}')
    print('O grupo é considerado IDOSO')