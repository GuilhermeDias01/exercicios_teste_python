# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

valor_idade = []
valor_altura = []

for i in range(5):

    idade = int(input('Informe a idade: '))
    altura = float(input('Informe a altura: '))
    
    valor_idade.append(idade)
    valor_altura.append(altura)

print(valor_idade[::-1])
print(valor_altura[::-1])
