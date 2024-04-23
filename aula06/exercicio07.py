'''
Exercício 07:

n = 3
i, j = 1
Somatório de um somatório (1 / i, j) ** 2
'''

def somatorio(n:int) -> list:
    somas = [0, 0]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            somas[0] += (1 / i) ** 2
            somas[1] += j ** 2
    return somas

n = 3
somas = somatorio(n)

print(f'\nSOMATORIO: {somas[0]:.2f} e {somas[1]}\n')
