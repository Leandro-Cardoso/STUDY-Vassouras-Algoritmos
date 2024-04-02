'''
3. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado 
do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um 
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e 
depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado 
quando não for informado o nome do atleta. A saída do programa deve ser conforme o 
exemplo abaixo:

    Atleta: Elon Musk

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Resultado final:
    Atleta: Rodrigo Curvêllo
    Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    Média dos saltos: 5.9 m
'''

nome = input('\nDigite o nome do atleta: ')
distancias = []
n = 5

for i in range(n):
    distancia = float(input(f'Distância {i + 1}: '))
    distancias.append(distancia)

print('\nResultado final:')
print(f'Atleta: {nome}')
saltos = ''
for distancia in distancias:
    if distancias[n - 1] == distancia:
        saltos += str(distancia)
    else:
        saltos += str(distancia) + ' - '
print(f'Saltos: {saltos}')
media = sum(distancias) / n
print(f'Média dos saltos: {media:.1f} m\n')
