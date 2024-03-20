'''
9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

n = 10
numeros = []
soma_quadrados = 0

for i in range(n):
    numero = int(input(f'\nDigite o {i + 1}º número inteiro: '))
    numeros.append(numero)
    soma_quadrados += numero ** (1 / 2)

print(f'\nA soma do quadrado dos números {numeros}, é {soma_quadrados}\n')
