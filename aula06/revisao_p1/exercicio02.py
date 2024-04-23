'''
2. Elabore uma função para encontrar o maior elemento em uma lista.
'''

def maior(valores:list) -> float:
    maior_valor = valores[0]
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
    return maior_valor

valores = [10, 1, 5, 30, 15, 6]
maior_valor = maior(valores)

print(f'\nMaior valor: {maior_valor}\n')
