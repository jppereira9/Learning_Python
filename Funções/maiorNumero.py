# Exercício 8.1 - Escreva uma função que retorne o maior de dois números

def maximo(x, y): # Definindo a função
    if x > y:
        return x
    else:
        return y
    
# Invocando a função
print(f'{maximo(5, 6)}') # 6
print(f'{maximo(2, 1)}') # 2
print(f'{maximo(7, 7)}') # 7