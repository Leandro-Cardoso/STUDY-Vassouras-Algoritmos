'''
1. Escreva uma função recursiva que calcule o máximo divisor comum (MDC) de dois números inteiros a e b.
'''

def mdc(a:int, b:int) -> int:
    '''Retorna MDC dos numeros "a" e "b".'''
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

resultado = mdc(20, 24)
print(f'\nMDC: {resultado}\n')
