# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores

lista_de_valores = []

while True:
    valor = input("Digite um número ou 'S' para sair: ")

    if valor.upper() == "S":
        break

    lista_de_valores.append(float(valor))

menorvalor = lista_de_valores[0]
maiorvalor = lista_de_valores[0]
soma = 0

#menor
for valor in lista_de_valores:
    if valor < menorvalor:
        menorvalor = valor

#maior
for valor in lista_de_valores:
    if valor > maiorvalor:
        maiorvalor = valor

#soma
for valor in lista_de_valores:
    soma += valor

print(menorvalor)
print(maiorvalor)
print(soma)             