'''
6. Escreva uma função recursiva que encontre todos os anagramas de uma string.
'''

# O fatorial do tamanho da string é o numero de possibilidade (n!)

def criar_anagramas(string:str) -> list:
    '''Retorna uma lista com todos os anagramas de uma string.'''
    string = string.lower()
    anagramas = []
    n = len(string)

    if n == 1:
        return [string]
    
    for i in range(n):
        nova_string = string[:i] + string[i + 1:]
        novos_anagramas = criar_anagramas(nova_string)
        for novo_anagrama in novos_anagramas:
            anagrama = string[i] + novo_anagrama
            if anagrama not in anagramas:
                anagramas.append(anagrama)
    return anagramas

anagramas = criar_anagramas('Meu')

print('\nANAGRAMAS:')
for i, anagrama in enumerate(anagramas):
    print(f'     {i + 1} - {anagrama}')
print('\n')
