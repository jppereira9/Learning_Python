# Exercício 8.4 - Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A (base x altura) / 2)

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Invocando a função
print(f'{area_triangulo(6, 9)}')
print(f'{area_triangulo(5, 8)}')