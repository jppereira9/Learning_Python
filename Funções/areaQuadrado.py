# Exercício 8.3 - Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²)

def area_quadrado(x): # Definindo a função
    area = x ** 2
    return area

# Invocando a função
print(f'{area_quadrado(4)}')
print(f'{area_quadrado(9)}')