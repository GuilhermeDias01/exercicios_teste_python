# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

vezes = int(input('Informe a quantidade de vezes deseja: '))
lista1 = []
x , y = 1, 1

for i in range(vezes):
    lista1.append(x)
    x , y = y , x + y
    
print(lista1)

