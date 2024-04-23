'''
Exercício 03:

Somatório de (i + 1) ** 3
'''

def somatorio(n:int) -> float:
    soma = 0
    for i in range(1, n + 1):
        soma += (i + 1) ** 3
    return soma

n = 2
soma = somatorio(n)

print(f'\nSOMATORIO: {soma:.2f}\n')
