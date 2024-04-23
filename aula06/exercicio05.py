'''
Exercício 05:

Somatório de (i + j) ** 2
'''

def somatorio(n:int, j:int) -> float:
    soma = 0
    for i in range(1, n + 1):
        soma += (i + j) ** 2
    return soma

n = 2
j = 1
soma = somatorio(n, j)

print(f'\nSOMATORIO: {soma:.2f}\n')
