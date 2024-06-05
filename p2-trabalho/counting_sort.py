'''
COUNTING SORT:
    Algoritmo para ordenar uma lista com base em na contagem de elementos dessa lista.

Vantagem:
    Muito mais eficiente que os algoritmos "selection", "bubble" e o "insertion".
    É um dos algoritmos mais eficientes.
    Velocidade linear.

Desvantagens:
    Algoritmo um pouco mais complexo de entender e não é amigavél para iniciantes.
    Ordena apenas numeros inteiros, precisa de uma adaptação para trabalhar com strings.

Passo a passo:
    Começar uma nova lista com o alcance da lista original iniciando com o valor 0 em todos os elementos.
    No incide correspondente ao valor de cada elemento da lista original, é colocado o quanto o valor original se repete na lista.
    Nessa nova lista, fazer a soma do elemeto anterior com o da posição atual e atualizar o valor, repetir esse processo em toda lista.
    Criar nova lista com mesmo tamanho da original.
    Ler lista original de trás para frente e colocar o valor dessa lista na posição definida pelo valor no indice correspondente ao valor original na primeira lista criada.
    Conforme for adicionando nas posições, tirar 1 nos valores correspondentes na primeira lista criada.
'''

def counting_sort(arr:list) -> list:
    max_val = max(arr)
    count = [0] * (max_val + 1)
    while len(arr) > 0:
        i = arr.pop(0)
        count[i] += 1
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
    return arr

if __name__ == '__main__':
    lista = [10, 5, 7, 1, 8, 9, 4, 2, 3, 6]
    counting_sort(lista)
    print(f'\nLista ordenada: {lista}\n')
