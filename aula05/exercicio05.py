'''
5. Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.
'''

def somar_digitos(numero:int, somatorio:int = 0) -> int:
    '''Retorna a soma dos digitos de um numero inteiro.'''
    numero = str(numero)
    if len(numero) == 0:
        return 0
    else:
        somatorio += 1
        return somatorio + somar_digitos(numero[:len(numero) - 1])

resposta = somar_digitos(1234500)
print(f'\nNumero de digitos: {resposta}\n')
