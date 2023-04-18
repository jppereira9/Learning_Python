# Para definir uma função, devemos utilizar o comando def

def soma(a, b): # Definindo a função
    print(f'{a + b}') # Somando os parâmetros a e b, mas não retorna nenhuma valor

# Invocando a função
soma(2, 9) # 11
soma(7, 8) # 15
soma(10, 15) # 25

'''
O exemplo anterior utiliza dois parâmetro e imprime sua soma. Essa função não retorna
valores como a função len ou a int. Vamos reescrever essa função de forma que o valor da soma
seja retornado

'''

def soma_2(c, d): # Definindo a função
    return c + d # Retorna a soma do parâmetro c e d

# Invocando a função
print(f'{soma_2(2, 9)}') # 11


