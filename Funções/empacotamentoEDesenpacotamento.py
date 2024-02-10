# Outra flexibilidade é passar parâmetros em pacotados em uma lista:

def soma (a, b): # Definindo a função
    print(a + b)

L = [2, 3] # Lista com valores
soma (*L) # Desempacotamento da lista
print("\n")

def barra (n = 10, c ="*"): # Definindo a função
    print(c * n)

L = [[5, "-"], [10, "*"], [5], [6, "*"]] # Lista de listas

for e in L:
    barra(*e)


