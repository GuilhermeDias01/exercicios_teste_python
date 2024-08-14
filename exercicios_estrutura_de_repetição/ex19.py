# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista_de_valores = []

while True:
    valor = input("Digite um número ou 'S' para sair: ")

    if valor.upper() == "S":
        break

    if float(valor) > 0 and float(valor) < 1000:
        lista_de_valores.append(float(valor))
    else:
        continue

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