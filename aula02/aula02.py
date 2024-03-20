'''
AULA 02:

- Explicação da lista de exercícios anterior.
- Testar todas as funções de uma lista.

1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
Extra: Depois adicione em uma função.
'''

def criar_vetor(n:int) -> list:
    '''Cria uma lista de "n" numeros inteiros.'''
    lista = []

    for i in range(n):
        numero = int(input(f'Digite o {i + 1}º número inteiro: '))
        lista.append(numero)

    return lista

#resultado = criar_vetor(5)
#print(f'\nNumeros: {resultado}\n')

'''
3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
Extra: Se média maior ou igual a 7 mostrar "aprovado" se não mostrar "reprovado".
'''

notas = []
n = 4

for i in range(n):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    notas.append(nota)

somatorio = sum(notas)
media = somatorio / n

print(f'\nAs notas são: {notas}')
print(f'A média das notas é: {media}\n')

if media >= 7:
    print('Aprovado !!!\n')
else:
    print('Reprovado !!!\n')
