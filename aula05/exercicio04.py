'''
4. Escreva uma função recursiva que verifique se uma string é um palíndromo. Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente, ignorando espaços, maiúsculas e minúsculas. Por exemplo, "arara" é um palíndromo.
'''

def string_reversa(string:str, i:int = 0) -> str:
    '''Retorna a string invertida.'''
    if i == len(string):
        return ''
    return string_reversa(string, i + 1) + string[i]

def is_palindromo(string:str) -> bool:
    '''Retorna se a string é um palíndromo ou não.'''
    string = string.lower()
    reversa = string_reversa(string)
    if reversa == string:
        return True
    else:
        return False

resposta = is_palindromo('Ovo')
print(f'\nÉ um palíndromo: {resposta}\n')
