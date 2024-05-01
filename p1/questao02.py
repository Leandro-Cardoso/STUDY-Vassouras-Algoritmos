'''
2. Escreva uma função que receba uma lista ordenada como parâmetro e retorne uma nova lista contendo apenas os números ímpares, e outra lista com os números pares da lista original.
Considere: Lista [1,2,3, ... , 10000]
'''

def numeros_impares_e_pares(numeros:list) -> list:
    impares = []
    pares = []
    for numero in numeros:
        if numero % 2 == 1:
            impares.append(numero)
        elif numero % 2 == 0:
            pares.append(numero)
    return [impares, pares]

numeros = []
for i in range(1, 10001):
    numeros.append(i)

dois_resultados = numeros_impares_e_pares(numeros)
impares = dois_resultados[0]
pares = dois_resultados[1]

print(f'\nNumeros ímpares: {impares}')
print(f'Numeros pares: {pares}\n')
