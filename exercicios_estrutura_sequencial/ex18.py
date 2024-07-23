#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo_mb = int(input('Informe o tamanho do arquivo em (MB): '))
velocidade_do_link_mbps = int(input('Informe a velocidade do link utilziado em (Mbps): '))

tempo_download = int(tamanho_arquivo_mb / (velocidade_do_link_mbps / 8 ))
minutos_usado = int(tempo_download / 60)
segundos_usados = tempo_download - (minutos_usado * 60)


print(f'O tempo de download utilizado foi de {minutos_usado} minutos e {segundos_usados} segundos.')