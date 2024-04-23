'''
4. Elabore uma função para calcular as raízes da equação do segundo grau.
'''

from math import sqrt

def delta(a:float, b:float, c:float) -> float:
    return b ** 2 - 4 * a * c

def bhaskara(a:float, b:float, c:float) -> any:
    d = delta(a, b, c)
    if d == 0:
        return -b / (2 * a)
    elif d < 0:
        return '∄'
    else:
        x1 = (sqrt(d) - b) / (2 * a)
        x2 = (-sqrt(d) - b) / (2 * a)
        return [x1, x2]

a = 1
b = -3
c = -10

raizes = bhaskara(a, b, c)

if type(raizes) is float:
    print(f'\nA raíz é {raizes:.1f}\n')
elif type(raizes) is str:
    print(f'\n{raizes}: Não existe raíz.\n')
else:
    print(f'\nAs raízes são {raizes[0]:.1f} e {raizes[1]:.1f}\n')
