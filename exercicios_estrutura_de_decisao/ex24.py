'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

valor1 = float(input('Digite o numero inteiro: '))
valor2 = float(input('Digite o numero inteiro: '))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")

def verifica():
    print(f'O resultado da operação selecionado é de: {resultado:.2f};')

    if resultado % 2 == 0:
        print('O Valor é Par;')
    else:
        print('O Valor é Impar;') 

    if resultado > 0:
            print('O Valor é Positivo;')   
    else:
         print('O Valor é Negativo;')  

    resultado_round = round(resultado, 2)

    if resultado == resultado_round:
        print('Inteiro;')
    else:
        print('Decimal;')   
          
if operacao == '+':
    resultado = valor1 + valor2
    verifica()
elif operacao == '-':
    resultado = valor1 - valor2
    verifica()
elif operacao == '/':
    resultado = valor1 / valor2
    verifica()
elif operacao == '*':
    resultado = valor1 * valor2
    verifica()