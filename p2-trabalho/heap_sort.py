'''
HEAP SORT:
    Algoritmo para ordenar uma lista com base em uma estrutura nomeada de Heap para préviamente organizar os elementos.

Vantagem:
    Muito mais eficiente que os algoritmos "selection", "bubble" e o "insertion" e com um nivél médio de dificuldade de compreenção.

Desvantagens:
    Algoritmo um pouco mais complexo de entender e não é amigavél para iniciantes.

Passo a passo:
    Converte a lista em um Heap.
    Defini o maior ou o menor elemento como raiz.
    Coloca os elementos do Heap no final da lista de forma ordenada.
'''

def heapify(lista:list, n:int, i:int) -> list:
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    if esquerda < n and lista[i] < lista[esquerda]:
        maior = esquerda
    if direita < n and lista[maior] < lista[direita]:
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)
    return lista

def heap_sort(lista:list) -> list:
    n = len(lista)
    for i in range(n // 2, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    heap_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
