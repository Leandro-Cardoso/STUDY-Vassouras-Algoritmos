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

def selection_sort(lista:list) -> list:
    n = len(lista)
    for i in range(n - 1):
        j_menor = i
        for j in range(i, n):
            if lista[j] < lista[j_menor]:
                j_menor = j
        if lista[j_menor] < lista[i]:
            lista[j_menor], lista[i] = lista[i], lista[j_menor]
    return lista

lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]

lista_ordenada = selection_sort(lista)

print(f'\nLista ordenada: {lista_ordenada}\n')
