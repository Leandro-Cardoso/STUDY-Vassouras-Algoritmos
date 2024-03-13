'''
7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

n = 5
numeros = []
soma = 0
multiplicacao = 1

for i in range(n):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    numeros.append(numero)
    soma += numero
    multiplicacao *= numero

print(f'\nOs números são: {numeros}')
print(f'A soma é: {soma}')
print(f'A multiplicação é: {multiplicacao}\n')
