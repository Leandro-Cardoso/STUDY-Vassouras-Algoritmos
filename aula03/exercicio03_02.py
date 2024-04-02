'''
2. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser 
armazenado). Após esta entrada de dados, faça:

    a. Mostre a quantidade de valores que foram lidos;
    b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do 
    outro;
    d. Calcule e mostre a soma dos valores;
    e. Calcule e mostre a média dos valores;
    f. Calcule e mostre a quantidade de valores acima da média calculada;
    g. Calcule e mostre a quantidade de valores abaixo de sete;
    h. Encerre o programa com uma mensagem;
'''

def lista_valores() -> list:
    valores = []

    print('\nDigite "-1" para terminar lista.\n')

    while True:
        valor = float(input('Digite o valor da nota: '))

        if valor == -1:
            break
        else:
            valores.append(valor)
    
    return valores

valores = lista_valores()

quantidade = len(valores)
print(f'\nQuantidade de valores: {quantidade}')

valores_ordenados = ''
for valor in valores:
    valores_ordenados += f' {valor} '
print(f'Valores digitados: {valores_ordenados}')

valores_inversos = reversed(valores)
print('Valores na ordem inversa:')
for valor in valores_inversos:
    print(f'{valor:.1f}')

soma = sum(valores)
print(f'Soma: {soma:.1f}')

media = soma / quantidade
print(f'Média: {media:.1f}')

acima_media = 0
for valor in valores:
    if valor > media:
        acima_media += 1
print(f'Valores acima da média: {acima_media}')

abaixo_7 = 0
for valor in valores:
    if valor < 7:
        abaixo_7 += 1
print(f'Valores abaixo de 7: {abaixo_7}')

print('\nObrigado !!!\n')
