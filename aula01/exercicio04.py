'''
4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

vetor = []
n = 10
todas_consoantes = ['a', 'e', 'i', 'o', 'u']
caracter = ''
consoantes = []

for i in range(n):
    while len(caracter) != 1:
        caracter = str(input('Digite um caracter: '))
        caracter.lower()
        if len(caracter) == 1:
            vetor.append(caracter)
        else:
            print('Digite apenas 1 caracter...')
    caracter = ''

for char in vetor:
    if char in todas_consoantes:
        consoantes.append(char)

print(f'Foram lidas {len(consoantes)} consoantes.')
print(f'Consoantes: {consoantes}')
