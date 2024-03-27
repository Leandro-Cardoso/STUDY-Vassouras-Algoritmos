'''
Aula 03:

Uso de bibliotecas, operadores matemáticos e casting (conversão de tipo de saída).

Função para arredondamento para cima: math.ceil(x)
Função para arredondamento para baixo: math.floor(x)
Função para potencia: math.pow(x, y) --------> x**y
'''

import math

x = 81
raiz_quadrada = math.sqrt(x)
raiz_quadrada_inteira = int(raiz_quadrada)

print(f'\nA raíz quadrada de {x} é {raiz_quadrada}, e a raíz inteira é {raiz_quadrada_inteira}.\n')
