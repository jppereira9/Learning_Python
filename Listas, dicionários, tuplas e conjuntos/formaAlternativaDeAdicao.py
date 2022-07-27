L = [] # A lista L é vazia
print(L) # Imprime a lista L(lista vazia)
print(len(L)) # Imprime o tamanho da lista L(O)
print("\n")

L = L + [1] # Adicionando 1 à lista
print(L) # Imprime o valor 1 da lista
print(len(L)) # Imprime o tamanho da lista L(1)
print("\n")

L = L + [2] # Adicionando 2 à lista
print(L) # Imprime o valor 1, 2 da lista
print(len(L)) # Imprime o tamanho da lista L(2)
print("\n")

L += [3, 4, 5]
print(L) # Imprime o valor 1, 2, 3, 4, 5 da lista
print(len(L)) # Imprime o tamanho da lista L(5)
print("\n")

# Utilizando o extend

L = ["a"] # Lista L
L.append("b") # Adicionando "b" à lista
print(L) # Imprime a lista L
print("\n")

L.extend(["c"]) # Adicionando c à lista
print(L) # Imprime a lista L
print("\n")

L.append(["d", "e"]) # Adicionando a lista ["d", "e"] à lista L
print(L) # Imprime a lista L
print("\n")

L.extend(["f", "g", "h"]) # Adicionando f, g, h à lista
print(L) # Imprime a lista L

'''

- O método extend sequer aceita parâmetros que não sejam listas. Se você utilizar o método append com uma lista 
como parâmetro, em vez de adicionar os elementos no fim da lista, append adicionára a lista inteira, mas como
apenas um novo elemento. Isso ocorre na linha 32

'''


