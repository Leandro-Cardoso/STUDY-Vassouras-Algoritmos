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

def heapify(arr:list, n:int, i:int) -> list:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    return arr

def heap_sort(arr:list) -> list:
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    heap_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
