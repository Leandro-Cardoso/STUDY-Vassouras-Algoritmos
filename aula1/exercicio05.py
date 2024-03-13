'''
5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

n = 20
numeros = []
pares = []
impares = []

for i in range(n):
    numero = int(input(f'Digite o {i + 1}° número inteiro: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'\nNumeros: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}\n')
