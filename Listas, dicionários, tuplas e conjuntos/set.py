'''
Conjuntos, set em python, são uma estrutura de dados que implementam operações de união,
intersecção e diferença, entre outras.

'''
# Algumas operações com conjuntos:
a = set()
a.add(1)
a.add(2)
a.add(3)
print(a) # Conjunto {1, 2, 3}

a.add(0)
a.add(-1)
print(a)

# Podemos testar se um elemento faz parte de um conjunto usando o operador in:
print(1 in a)
print(10 in a)
print(2 in a)

# Um set(conjunto) pode ser criado a partir de listas, tuplas e qualquer outra estrutura de dados que seja enumerável
b = set([2, 3])
print(b)

# Entre as operações disponíveis com conjuntos, temos a diferença entre conjuntos, que utiliza o operador -
a = {0, 1, 2, 3, -1}
b = {2, 3}
print(a - b)

# A união é realizada pelo operador |
a = {0, 1, 2, 3, -1}
b = {2, 3}
print(a | b)

c = set([4, 5, 6])
print(a | c)