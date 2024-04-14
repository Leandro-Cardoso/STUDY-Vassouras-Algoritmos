'''
2. Escreva uma função recursiva que calcule a potência de um número x elevado a um expoente n.
'''

def potencia(x:float, n:float) -> float:
    '''Retorna a potência de "x" elevado a "n".'''
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * potencia(x, n - 1)

resultado = potencia(5, 3)
print(f'\nPotência: {resultado:.1f}\n')
