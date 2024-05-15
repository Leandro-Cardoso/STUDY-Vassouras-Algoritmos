'''
Faça um algoritmo de busca que:

Dada uma lista = [20, 5, 15, 24, 67, 1, 76, 21, 11]
Se encontrar a chave = 45, retorne a posição.
Se não, retorne -1.
'''

def busca(lista:list, chave:int) -> int:
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    return -1

lista = [20, 5, 15, 24, 67, 1, 45, 76, 21, 11]
chave = 45

resultado = busca(lista, chave)

if resultado == -1:
    print('\nChave não encontrada.\n')
else:
    print(f'\nResposta: {resultado}\n')
