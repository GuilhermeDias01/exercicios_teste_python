# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de # B seja 200000 habitantes 
# com uma taxa de crescimento de 1.5%. # Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
# A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a = 80000
pop_b = 200000
taxa_cres_a = 0.03
taxa_cres_b = 0.015
contador = 0

while pop_a <= pop_b:
    pop_a += pop_a * taxa_cres_a
    pop_b += pop_b * taxa_cres_b
    contador += 1

print(f'A quanidade da anos necessária foi de: {contador} anos')

