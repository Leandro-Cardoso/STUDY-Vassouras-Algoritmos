'''
INSERTION SORT:
    Algoritmo para ordenar uma lista com base na inserção de cada elemento dessa lista.

Vantagem:
    Fácil de entender o funcionamento, satisfatorio para listas pequenas e boa para iniciantes.

Desvantagens:
    Não é eficiente com listas grandes, pois é necessário percorrer toda a lista por varias vezes.

Passo a passo:
    Começando do segundo elemento de uma lista, compare com o anterior. Se maior, mantem a posição, se menor, trocam de posição.
    Repetir processo até que fique na posição correta.
    Seguir os mesmos passos com os próximos elementos da lista, até o final.
'''

def insertion_sort(lista:list) -> list:
    n = len(lista)
    for i in range(1, n):
        elemento = lista[i]
        i_ant = i - 1
        while i_ant >= 0 and lista[i_ant] > elemento:
            lista[i_ant + 1] = lista[i_ant]
            i_ant -= 1
        lista[i_ant + 1] = elemento
    return lista

lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]

lista_ordenada = insertion_sort(lista)

print(f'\nLista ordenada: {lista_ordenada}\n')
