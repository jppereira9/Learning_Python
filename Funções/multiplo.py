# Exercício 8.2 - Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo

def multiplo(x, y): # Definindo a função
    if x % y == 0:
        return True
    else:
        return False

# Invocando a função
print(f'{multiplo(8, 4)}') # True
print(f'{multiplo(7, 3)}') # False
print(f'{multiplo(5, 5)}') # True