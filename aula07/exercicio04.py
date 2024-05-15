'''
Utilize a busca binária para encontrar a chave 45 na lista [1, 5, 15, 20, 24, 45, 67, 76, 78, 100].
'''

def busca_binaria(lista:list, chave:int) -> int:
    inicio = 0
    fim = len(lista) - 1
    while fim != 0:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

lista = [1, 5, 15, 20, 24, 45, 67, 76, 78, 100]
chave = 45

resultado = busca_binaria(lista, chave)

if resultado == -1:
    print('\nChave não encontrada.\n')
else:
    print(f'\nIndice: {resultado}\n')
