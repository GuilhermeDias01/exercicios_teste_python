'''
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, 
linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
eles devem ser modificados para valores dentro da faixa de forma elegante.
'''

def verifica_valor(n):
    if n == '':
        return(int(1))
    else:
        return(verifica_valor_min_e_max(n))


def verifica_valor_min_e_max(n):
    if n < 1:
        return(int(1))
    elif n > 20:
        return(int(20))
    else:
        return(int(n))

def desenha_linha(linha):
    l='+'
    for x in range(linha):
        l+='-'
    l+='+'
    print (l)

def desenha_coluna(linha,coluna):
      for y in range(coluna):
        c='|'
        c+= ' '*linha
        c+='|'
        print (c) 

def desenha_moldura(linha,coluna):
    desenha_linha(linha)
    desenha_coluna(linha,coluna)
    desenha_linha(linha)


linha=int(input('Diga quantos +----+, entre 1 e 20: '))
coluna=int(input('Diga quantos |    |, entre 1 e 20: '))

desenha_moldura(verifica_valor(linha), verifica_valor(coluna))
