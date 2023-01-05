# Tuplas pode ser vistas como lista em Python, com a grande diferença de serem imutáveis

tupla = ("a", "b", "c")
print(tupla)

# Parênteses são opcionais:
tupla_2 = "a", "b", "c"
print(tupla_2)

# Tuplas suportam a maior parte das operações de lista, como fatiamento e indexação:
tupla_3 = ("a", "b", "c")
print(tupla_3[0]) # Índice 1
print(tupla_3[2]) # Índice 2
print(tupla_3[1:]) # Fatiamento a partir do índice 1
print(tupla_3 * 2)

# Tuplas não podem ter seus elementos alterados
# tupla_3[0] = "Banana" - Erro

# Várias funções utilizam ou geram tuplas em python. Tuplas podem ser utlizadas com for
for elemento in tupla_3:
    print(elemento)

# Empacotamento
tupla_4 = 100, 200, 300
print(tupla_4)

# Desempacotamento
a, b = 10, 20
print(a)
print(b)

# Troca de elementos com tuplas
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# Tupla com único elemento
t1 = (1)
print(t1)
t2 = (1,)
print(t2)
t3 = 1,
print(t3)

# Tupla vazia
t4 = ()
print(t4)
print(len(t4))

# Tuplas também podem ser criadas a partir de lista, utilizando a função tuple
L = [1, 2, 3]
t = tuple(L)
print(t)

# Concatenação de tuplas
t_1 = (1, 2, 3)
t_2 = (3, 4, 5)
print(t_1 + t_2)

# Tuplas com listas internas
tupla_x = ("a", ["b", "c", "d"])
print(tupla_x)
print(len(tupla_x))
print(tupla_x[1])
tupla_x[1].append("e")
print(tupla_x)

# Desempacotamento com listas
c, d = 1, 2
print(c, d)
d, e = [5, 6]
print(d, e)

# Podemos usar o * para indicar vários valores a desempacotar
*a, b = [1, 2, 3, 4, 5]
print(a)

print(b)

a, *b = [1, 2, 3, 4, 5]
print(a)
print(b)