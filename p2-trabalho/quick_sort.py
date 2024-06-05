'''
QUICK SORT:
    Algoritmo para ordenar uma lista com base em um elementos aleatório (pivo) dessa lista.

Vantagem:
    Muito mais eficiente que os algoritmos "selection", "bubble" e o "insertion".

Desvantagens:
    Algoritmo um pouco mais complexo de entender e não é amigavél para iniciantes. 

Passo a passo:
    Definir um elemento como pivo.
    Verificar cada elemento da lista.
    Passa elementos maiores que o pivo para direita e os menores para a esquerda, gravando a posição entre eles.
    No final trocar a posição do pivo para essa posição intermediária.
    Repetir todo o processo anterior para as sublistas dos menores e para a dos maiores, até que o tamanho das sublistas seja de 1 elemento.
'''

def partition(arr:list, start:int = 0, end:int = None) -> int:
    pivo = arr[end]
    i = start
    for j in range(start, end):
        if arr[j] <= pivo:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i

def quick_sort(arr:list, start:int = 0, end:int = None) -> list:
    if end is None:
        end = len(arr) - 1
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    quick_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
