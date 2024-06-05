'''
BUBBLE SORT:
    Algoritmo para ordenar uma lista com base na troca de cada elemento.

Vantagem:
    Fácil de entender o funcionamento, satisfatorio para listas pequenas e boa para iniciantes.

Desvantagens:
    Não é eficiente com listas grandes, pois é necessário percorrer toda a lista por varias vezes.
    A eficiencia cai exponencialmente de acordo com o tamanho da lista.

Passo a passo:
    Compara o primeiro com o segundo elemento, se o primeiro for maior que o segundo elemento, eles trocam de posição.
        Segue essa ação para todos os elementos da lista.
    No final. Se algum elemento tiver sido trocado ele repete a primeira ação de comparação e troca para todos os elementos da lista novamente.
        Segue essa ação até que não exista mais trocas a serem feitas.
    Por fim, é retornada a lista ordenada.
'''

def bubble_sort(arr:list) -> list:
    change = True
    n = len(arr)
    while change:
        change = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    bubble_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
