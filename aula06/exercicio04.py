'''
Exercício 04:

Somatório de i ** 3 / i
'''

def somatorio(n:int) -> float:
    soma = 0
    for i in range(1, n + 1):
        soma += i ** 3 / i
    return soma

n = 2
soma = somatorio(n)

print(f'\nSOMATORIO: {soma:.2f}\n')
