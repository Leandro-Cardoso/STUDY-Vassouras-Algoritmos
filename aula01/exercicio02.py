'''
2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

vetor = []

for i in range(10):
    numero = float(input(f'Digite o {i + 1}º número inteiro: '))
    vetor.append(numero)

vetor.reverse()
print(f'\nNumeros: {vetor}\n')
