'''
- Listas são um tipo de variável que permite o armazenamento de vários valores, acessados por um índice.
Uma lista pode conter zero ou N elementos de um mesmo tipo ou de tipos diversos, podendo conter outras 
listas. O tamanho de uma lista é igual à quantidade de elementos que ela contém.

'''

# Vejamos como criar uma lista em Python:
L = [] # Essa linha cria uma lista chamada L com zero elementos, ou seja, uma lista vazia

# A lista Z possui 3 elementos
Z = [15, 8, 9] # O tamanho da lista é 3

print(Z[0]) # Índice 0
print(Z[1]) # Índice 1
print(Z[2]) # Índice 2

# Utilizando o nome da lista e um índice, podemos mudar o conteúdo de um elemento:
Z[0] = 23
print(Z)

