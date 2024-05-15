'''
Refaça a função utilizando enumerate().
'''

def busca(lista:list, chave:int) -> int:
    for i, elemento in enumerate(lista):
        if elemento == chave:
            return i
    return -1

lista = [20, 5, 15, 24, 67, 1, 45, 76, 21, 11]
chave = 45

resultado = busca(lista, chave)

if resultado == -1:
    print('\nChave não encontrada.\n')
else:
    print(f'\nIndice: {resultado}\n')
