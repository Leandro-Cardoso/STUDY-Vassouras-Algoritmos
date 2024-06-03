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

def particionar(lista:list, inicio:int = 0, fim:int = None) -> int:
    pivo = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def quick_sort(lista:list, inicio:int = 0, fim:int = None) -> list:
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = particionar(lista, inicio, fim)
        quick_sort(lista, inicio, p - 1)
        quick_sort(lista, p + 1, fim)

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    quick_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
