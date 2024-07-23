# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
# excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

peso_limete = 50
multa = 4.00

peso_dos_peixes_pescador = input('Digite o peso dos peixes obtidos: ')

peso_dos_peixes_pescador_float = float(peso_dos_peixes_pescador)

if peso_dos_peixes_pescador_float > 50.0:
    execesso_peso = peso_dos_peixes_pescador_float - peso_limete
    valor_a_pagar = multa * execesso_peso
    print(f'O exesso do peso é de: {execesso_peso}')
    print(f'O valor da multa ser pago é de: {valor_a_pagar}')
else:   
    print('O peso não ultrapassa o limite estipulado, carga liberada.')
