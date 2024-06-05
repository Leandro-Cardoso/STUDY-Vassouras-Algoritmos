'''
MERGE SORT:
    Algoritmo para ordenar uma lista com base na separação e junção dos elementos dessa lista.

Vantagem:
    Muito mais eficiente que os algoritmos "selection", "bubble" e o "insertion".

Desvantagens:
    Algoritmo um pouco mais complexo de entender e não é amigavél para iniciantes. 

Passo a passo:
    Dividir a lista em 2 sublistas.
    Dividir as sublistas em mais 2 sublistas cada.
    Repetir esse passo até o menor tamanho.
    Juntar duas sublistas de menor tamanho de forma ordenada.
    Repetir esse passo com as restantes.
    Depois juntar duas sublistas resultantes de forma ordenada novamente, comparando os primeiros elementos e ordenando, até o final.
    Repetir esse processo até que reste apenas uma lista já ordenada.
'''

def merge(arr:list, start:int, middle:int, end:int) -> list:
    half_1 = arr[start : middle]
    half_2 = arr[middle : end]
    top_1 = 0
    top_2 = 0
    for i in range(start, end):
        if top_1 >= len(half_1):
            arr[i] = half_2[top_2]
            top_2 += 1
        elif top_2 >= len(half_2):
            arr[i] = half_1[top_1]
            top_1 += 1
        elif half_1[top_1] < half_2[top_2]:
            arr[i] = half_1[top_1]
            top_1 += 1
        else:
            arr[i] = half_2[top_2]
            top_2 += 1
    return arr

def merge_sort(arr:list, start:int = 0, end:int = None) -> list:
    if end is None:
        end = len(arr)
    if end - start > 1:
        middle = (end + start) // 2
        merge_sort(arr, start, middle)
        merge_sort(arr, middle, end)
        merge(arr, start, middle, end)
    return arr

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    merge_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
