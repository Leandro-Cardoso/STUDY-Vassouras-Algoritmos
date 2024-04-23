'''
Exercício 06:

n = 3
i, j = 1
Somatório de um somatório (i + j)
'''

def somatorio(n:int) -> int:
    soma = 0
    for i in range(1, n + 1):
        soma_interna = 0
        for j in range(1, n + 1):
            soma_interna += i + j
        soma += soma_interna
    return soma

n = 3
soma = somatorio(n)

print(f'\nSOMATORIO: {soma}\n')
