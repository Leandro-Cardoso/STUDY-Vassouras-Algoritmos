'''
4. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em 
galões de 3,6 litros, que custam R$ 25,00.

    • Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
    preços em 3 situações:
    • comprar apenas latas de 18 litros;
    • comprar apenas galões de 3,6 litros;
    • misturar latas e galões, de forma que o desperdício de tinta seja 
    menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto 
    é, considere latas cheias.
'''

from math import ceil

def quantidade_latas(area_pintada:float) -> dict:
    cobertura = area_pintada * 6
    latas_grandes = ceil(cobertura / 18)
    if latas_grandes * 18 + 3.6 * 3 < cobertura:
        valor = latas_grandes * 80
    else:
        latas_grandes -= 1
        latas_pequenas = ceil((cobertura - latas_grandes * 18) / 3.6)
        valor = latas_grandes * 80 + latas_pequenas * 25
    return {
        'latas_grandes' : latas_grandes,
        'latas_pequenas' : latas_pequenas,
        'valor' : valor
    }

area_pintada = float(input('\nQuantos metros quadrados a ser pintado: '))

tabela = quantidade_latas(area_pintada)

print(f'\nQuantidade de latas grandes: {tabela["latas_grandes"]}')
print(f'Quantidade de latas pequenas: {tabela["latas_pequenas"]}')
print(f'Valor total: R$ {tabela["valor"]:.2f}\n')
