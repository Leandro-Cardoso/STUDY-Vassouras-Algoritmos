'''
8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
'''

n = 5
idades = []
alturas = []

for i in range(n):
    idade = int(input(f'\nDigite a idade da {i + 1}ª pessoa: '))
    altura = float(input(f'Digite a altura da {i + 1}ª pessoa: '))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

print(f'\nIdades na ordem inversa: {idades}')
print(f'Alturas na ordem inversa: {alturas}\n')
