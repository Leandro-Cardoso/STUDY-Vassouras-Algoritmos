'''
5. Elaborar um programa Python para calcular a soma dos elementos de uma lista 
utilizando recursão.
'''

def somatorio(valores:list) -> float:
    i = len(valores)
    soma = 0
    if i == 0:
        return soma
    else:
        valor = valores[i - 1]
        soma += valor
        valores.remove(valor)
        return soma + somatorio(valores)

valores = [10, 5, 7, 3]
soma = somatorio(valores)

print(f'\nSOMATÓRIO: {soma:.1f}\n')
