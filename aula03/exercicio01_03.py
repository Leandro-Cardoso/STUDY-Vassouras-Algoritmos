'''
3. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe 
ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

from math import ceil

def quantidade_latas(area_pintada:float) -> dict:
    cobertura = area_pintada * 3
    latas = ceil(cobertura / 18)
    valor = latas * 80
    return {
        'latas' : latas,
        'valor' : valor
    }

area_pintada = float(input('\nQuantos metros quadrados a ser pintado: '))

tabela = quantidade_latas(area_pintada)

print(f'\nQuantidade de latas: {tabela["latas"]}')
print(f'Valor total: R$ {tabela["valor"]}\n')
