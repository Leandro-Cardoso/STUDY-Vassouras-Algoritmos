'''
Aula 06:

Revisão de loops e bibliotecas.
'''

def somatorio_quadrado(n:int, i:int = 1) -> int:
    '''Retorna o somatório do quadrado de um intervalo de números inteiros, de "i" até "n".'''
    somatorio = 0
    if i == n + 1:
        return somatorio
    else:
        somatorio += i ** 2
        return somatorio + somatorio_quadrado(n, i + 1)

n = 3
somatorio = somatorio_quadrado(n)

print(f'\nSOMATÓRIO: {somatorio}\n')
