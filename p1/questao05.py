'''
5. Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N.
'''

def somatorio(n:int) -> int:
    soma = 0
    if n == 0:
        return soma
    else:
        soma += n
        return soma + somatorio(n - 1)

n = 5
soma = somatorio(n)

print(f'\nSOMATÓRIO: {soma}\n')
