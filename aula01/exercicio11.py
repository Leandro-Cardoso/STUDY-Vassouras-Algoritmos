'''
11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

n = 10
vetor_a = []
vetor_b = []
vetor_c = []
vetor_abc = []

for i in range(3):
    for j in range(n):
        elemento = input(f'\nDigite o {j + 1}º elemento do vetor {i + 1}: ')
        if i == 0:
            vetor_a.append(elemento)
        elif i == 1:
            vetor_b.append(elemento)
        else:
            vetor_c.append(elemento)

for i in range(n):
    elemento_a = vetor_a[i]
    vetor_abc.append(elemento_a)
    elemento_b = vetor_b[i]
    vetor_abc.append(elemento_b)
    elemento_c = vetor_c[i]
    vetor_abc.append(elemento_c)

print(f'\nVetor 1: {vetor_a}')
print(f'Vetor 2: {vetor_b}')
print(f'Vetor 3: {vetor_c}')
print(f'Vetor de elementos intercalados: {vetor_abc}\n')
