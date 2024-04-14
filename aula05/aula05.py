'''
Aula 05:

Recursividade.

Material de apoio: https://joaoarthurbm.github.io/eda/posts/analise-algoritmos-recursivos/
'''

def fat(n:int) -> int:
    '''Retorna o fatorial de "n".'''
    if n == 0:
        return 1
    else:
        return n * fat(n - 1)

n = 5
fatorial = fat(n)

print(f'\nO fatorial de {n} é {fatorial}\n')

'''
def fatorial(n:int) -> int:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

n = int(input('\nn = '))
resultado = fatorial(n)
print(f'\nO fatorial de {n} é {resultado}\n')
'''
