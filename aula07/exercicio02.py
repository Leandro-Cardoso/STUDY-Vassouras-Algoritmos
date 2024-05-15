'''
Refaça a função sem utilizar lista[i].
'''

def busca(lista:list, chave:int) -> int:
    i = 0
    for elemento in lista:
        if elemento == chave:
            return i
        i += 1
    return -1

lista = [20, 5, 15, 24, 67, 1, 45, 76, 21, 11]
chave = 45

resultado = busca(lista, chave)

if resultado == -1:
    print('\nChave não encontrada.\n')
else:
    print(f'\nIndice: {resultado}\n')
