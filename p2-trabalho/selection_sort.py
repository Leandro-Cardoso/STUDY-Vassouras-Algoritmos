'''
SELECTION SORT:
    Algoritmo para ordenar uma lista com base no menor ou no maior elemento dessa lista.

Vantagem:
    Fácil de entender o funcionamento, satisfatorio para listas pequenas e boa para iniciantes.

Desvantagens:
    Não é eficiente com listas grandes, pois é necessário percorrer toda a lista por varias vezes.
    A eficiencia cai exponencialmente de acordo com o tamanho da lista.

Passo a passo:
    Encontrar o menor ou o maior elemento da lista e por como primeiro, trocando de posição.
    Encontrar segundo menor ou o maior elemento da lista e por como segundo, e assim por diante, até o último elemento.
'''

def selection_sort(arr:list) -> list:
    n = len(arr)
    for i in range(n - 1):
        j_min = i
        for j in range(i, n):
            if arr[j] < arr[j_min]:
                j_min = j
        if arr[j_min] < arr[i]:
            arr[j_min], arr[i] = arr[i], arr[j_min]
    return arr

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    selection_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
