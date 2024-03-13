'''
6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''

n_notas = 4
n_alunos = 10
medias = []
n_medias_boas = 0

for i in range(n_alunos):
    media = 0
    for j in range(n_notas):
        nota = float(input(f'Digite a {j + 1}ª nota do {i + 1}º aluno: '))
        media += nota / n_notas
    medias.append(media)
    if media >= 7:
        n_medias_boas += 1

print(f'\nSão {n_medias_boas} alunos com média igual ou superior a 7.\n')
