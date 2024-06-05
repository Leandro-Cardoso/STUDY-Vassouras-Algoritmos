'''
RADIX SORT:
    Algoritmo para ordenar uma lista com base em na contagem de cada digito de cada elemento dessa lista utilizando buckets.

Vantagem:
    Muito mais eficiente que os algoritmos "selection", "bubble" e o "insertion".
    É um dos algoritmos mais eficientes.
    Funciona tanto com números quanto com string.
    Velocidade linear.

Desvantagens:
    Algoritmo um pouco mais complexo de entender e não é amigavél para iniciantes. 

Passo a passo:
    Encontrar o valor máximo.
    Inicializar buckets.
    Agrupar por dígitos.
    Repetir passos até que esteja ordenado.
'''

def radix_sort(arr:list, base:int = 10) -> list:
    exp = 1
    max_val = max(arr)
    buckets = [list() for _ in range(base)]
    while max_val // exp > 0:
        while len(arr) > 0:
            val = arr.pop()
            i = val // exp % base
            buckets[i].append(val)
        for bucket in buckets:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)
        exp *= base
    return arr

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    radix_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
