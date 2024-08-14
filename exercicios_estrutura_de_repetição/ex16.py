# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500
vezes = int(input('Informe a quantidade de vezes deseja: '))
lista1 = []
x , y = 1, 1

for i in range(vezes):
    lista1.append(x)
    x , y = y , x + y
    if x > 500:
        break

print(lista1)
