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

def merge(lista:list, inicio:int, meio:int, fim:int) -> list:
    metade_1 = lista[inicio : meio]
    metade_2 = lista[meio : fim]
    topo_1 = 0
    topo_2 = 0
    for i in range(inicio, fim):
        if topo_1 >= len(metade_1):
            lista[i] = metade_2[topo_2]
            topo_2 += 1
        elif topo_2 >= len(metade_2):
            lista[i] = metade_1[topo_1]
            topo_1 += 1
        elif metade_1[topo_1] < metade_2[topo_2]:
            lista[i] = metade_1[topo_1]
            topo_1 += 1
        else:
            lista[i] = metade_2[topo_2]
            topo_2 += 1

def merge_sort(lista:list, inicio:int = 0, fim:int = None) -> list:
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista

lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]

lista_ordenada = merge_sort(lista)

print(f'\nLista ordenada: {lista_ordenada}\n')
