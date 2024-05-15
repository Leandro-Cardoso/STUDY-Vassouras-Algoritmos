'''
AULA 07:

Coleções:
   - Lista []
   - Tupla ()
   - Dicionário {'chave' : 'valor'}
   - Set {} (conjuntos - Não ordenado, imutável, sem indice)

Busca em listas.

Busca binária.

Trabalho P2 - Implementação:
Analisar, oque ele faz, vantagens, desvantagens e passo a passo de funcionamento de todos os algoritmos abaixo e implementar em Python.
   - Bubble Sort
   - Insertion Sort
   - Merge Sort
   - Quick Sort
   - Heap Sort
   - Counting Sort
   - Radix Sort
'''

print('')

# Set - Conjunto:
conjunto = {'a', 'b', 'c'}
for elemento in conjunto:
    print(elemento)
print(type(conjunto), '\n')

# Dicionário:
dicionario = {
    'Aluno 1' : 1,
    'Aluno 2' : 2,
    'Aluno 3' : 3
}
for chave, valor in dicionario.items():
    print(f' {chave} -> {valor}')
print(type(dicionario), '\n')
