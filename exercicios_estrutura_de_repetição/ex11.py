# Altere o programa anterior para mostrar no final a soma dos números.

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
soma = numero1 + numero2

if numero1 < numero2:

    for numeros in range(numero1 + 1, numero2):
        print(numeros)
        soma += numeros
    

else:
    
    for numeros in range(numero2 + 1 , numero1):
        print(numeros)
        soma += numeros
        
print(soma)