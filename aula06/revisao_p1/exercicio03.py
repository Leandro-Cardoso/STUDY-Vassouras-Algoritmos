'''
3. Elabore uma função para calcular a área de um triângulo, quadrado, retângulo, círculo, 
trapézio, losango.
'''

from math import pi

# Triângulo:
def area_triangulo(b:float, h:float) -> float:
    return b * h / 2

# Quadrado:
def area_quadrado(lado:float) -> float:
    return lado ** 2

# Retângulo:
def area_retangulo(a:float, b:float) -> float:
    return a * b

# Círculo:
def area_circulo(r:float) -> float:
    return pi * r ** 2

# Trapézio:
def area_trapezio(b_maior:float, b_menor:float, h:float) -> float:
    return (b_maior + b_menor) * h / 2

# Losango:
def area_losango(d_maior:float, d_menor:float) -> float:
    return d_maior * d_menor / 2

# Testes:
a = 5
b = 3
b_maior = 6
h = 2
r = 1
d = 2
d_maior = 4

triangulo = area_triangulo(b, h)
quadrado = area_quadrado(a)
retangulo = area_retangulo(a, b)
circulo = area_circulo(r)
trapezio = area_trapezio(b_maior, b, h)
losango = area_losango(d_maior, d)

print(f'\nArea do triânguro = b x h = {b} x {h} = {triangulo}')
print(f'Area do quadrado = l² = {a}² = {quadrado}')
print(f'Area do retângulo = a x b = {a} x {b} = {retangulo}')
print(f'Area do círculo = pi x r² = {pi:.2f} x {r}² = {circulo:.2f}')
print(f'Area do trapézio = (B + b) x h / 2 = ({b_maior} + {b}) x {h} / 2 = {trapezio}')
print(f'Area do losango = D x d / 2 = {d_maior} x {d} / 2 = {losango}\n')
