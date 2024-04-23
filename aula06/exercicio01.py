'''
Exercício 01:

Somatório de (1 / i) ** 2
'''

def somatorio(n:int) -> float:
    soma = 0
    for i in range(1, n + 1):
        soma += (1 / i) ** 2
    return soma

n = 2
soma = somatorio(n)

print(f'\nSOMATORIO: {soma:.2f}\n')
