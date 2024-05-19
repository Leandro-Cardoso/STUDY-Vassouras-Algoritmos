'''
BUBBLE SORT:
    Funão para ordenar uma lista com base na troca de cada elemento.

Vantagem:
    Fácil de entender o funcionamento, satisfatorio para listas pequenas e boa para iniciantes.

Desvantagens:
    Não é eficiente com listas grandes, pois é necessário percorrer toda a lista.

Passo a passo:
    Compara o primeiro com o segundo elemento, se o primeiro for maior que o segundo elemento, eles trocam de posição.
        Segue essa ação para todos os elementos da lista.
    No final. Se algum elemento tiver sido trocado ele repete a primeira ação de comparação e troca para todos os elementos da lista novamente.
        Segue essa ação até que não exista mais trocas a serem feitas.
    Por fim, é retornada a lista ordenada.
'''

def bubble_sort(lista:list) -> list:
    trocar = True
    while trocar:
        trocar = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocar = True
    return lista

lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]

lista_ordenada = bubble_sort(lista)

print(f'\nLista ordenada: {lista_ordenada}\n')
