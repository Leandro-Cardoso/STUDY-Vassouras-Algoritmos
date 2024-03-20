'''
1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

vetor = []

for i in range(5):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    vetor.append(numero)

print(f'\nNumeros: {vetor}\n')
