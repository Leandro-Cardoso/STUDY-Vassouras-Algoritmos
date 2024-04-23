'''
1. Utilize uma função que use Operadores Lógicos: and, or, not.
'''

def analisar(valor) -> str:
    valor = str(valor)
    try:
        valor = float(valor)
        if not valor % 2 == 0 and not valor % 2 == 1:
            if valor > 0:
                return f'\nO valor {valor} é um número fracionado positivo.\n'
            else:
                return f'\nO valor {valor} é um número fracionado negativo.\n'
        else:
            valor = int(valor)
            if valor >= 0:
                if valor % 2 == 1:
                    return f'\nO valor {valor} é um número inteiro, ímpar e positivo.\n'
                elif valor % 2 == 0 and valor >= 0:
                    return f'\nO valor {valor} é um número inteiro, par e positivo.\n'
            else:
                return f'\nO valor {valor} é um número inteiro e negativo.\n'
    except:
        if valor == 'True' or valor == 'False':
            return f'\nO valor {valor} é um booleano\n'
        else:
            return f'\nO valor {valor} é uma string\n'

valor = 6.0
resposta = analisar(valor)

print(resposta)
