'''
3. Escreva uma função recursiva que inverta uma string. Por exemplo, se a entrada for "python", a função deve retornar "nohtyp".
'''

def string_reversa(string:str, i:int = 0) -> str:
    '''Retorna a string invertida.'''
    if i == len(string):
        return ''
    return string_reversa(string, i + 1) + string[i]

resultado = string_reversa('lava')
print(f'\nString inversa: {resultado}\n')
