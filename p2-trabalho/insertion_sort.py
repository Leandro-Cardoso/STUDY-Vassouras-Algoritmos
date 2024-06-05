'''
INSERTION SORT:
    Algoritmo para ordenar uma lista com base na inserção de cada elemento dessa lista.

Vantagem:
    Fácil de entender o funcionamento, satisfatorio para listas pequenas e boa para iniciantes.

Desvantagens:
    Não é eficiente com listas grandes, pois é necessário percorrer toda a lista por varias vezes.
    A eficiencia cai exponencialmente de acordo com o tamanho da lista.

Passo a passo:
    Começando do segundo elemento de uma lista, compare com o anterior. Se maior, mantem a posição, se menor, trocam de posição.
    Repetir processo até que fique na posição correta.
    Seguir os mesmos passos com os próximos elementos da lista, até o final.
'''

def insertion_sort(arr:list) -> list:
    n = len(arr)
    for i in range(1, n):
        element = arr[i]
        i_ant = i - 1
        while i_ant >= 0 and arr[i_ant] > element:
            arr[i_ant + 1] = arr[i_ant]
            i_ant -= 1
        arr[i_ant + 1] = element
    return arr

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    insertion_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
