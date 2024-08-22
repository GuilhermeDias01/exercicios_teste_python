# Faça um programa com uma função chamada somaImposto. 

# A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.

# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(porcentagem, custo):
    valor_produto = custo + ((custo * porcentagem) / 100)
    return(valor_produto)

taxa = float(input('informe o valor da Taxa: '))
valor_de_custo = float(input('Informe o valor de custo do produto: '))

print(somaImposto(taxa,valor_de_custo))