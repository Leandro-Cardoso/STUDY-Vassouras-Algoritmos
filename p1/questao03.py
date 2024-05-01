'''
3. Crie uma função em Python que leia 80000 números e informe a média dos números. Utilize Funções.
'''

def media(numeros:list) -> float:
    somatorio = 0
    for numero in numeros:
        somatorio += numero
    return somatorio / len(numeros)

numeros = []
for i in range(1, 80001):
    numeros.append(i)

med = media(numeros)

print(f'\nMédia: {med:.1f}\n')
