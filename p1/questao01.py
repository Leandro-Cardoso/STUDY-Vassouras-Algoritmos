'''
1. Crie uma função chamada comprimentoMenor que recebe duas strings como parâmetros e retorna True se o comprimento da primeira string for menor do que o da segunda string, e False caso contrário.
'''

def comprimentoMenor(a:str, b:str) -> bool:
    if len(a) < len(b):
        return True
    else:
        return False

a = 'teste'
b = 'teste grande'
resposta = comprimentoMenor(a, b)

print(f'\nResposta: {resposta}\n')
