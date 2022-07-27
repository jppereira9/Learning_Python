L = [1, 2, 3, 4, 5] # Lista L
V = L # A lista V é igual a lista V

print("Lista L: {}" .format(L)) # [1, 2, 3, 4, 5]
print("Lista V: {}" .format(V)) # [1, 2, 3, 4, 5]

V[0] = 6 # Atribuindo o valor 6 ao 1] índice da lista, porém, temos um efeito colateral, o índice 0 na lista L será alterado também
print("\n")
print("Lista L: {}" .format(L)) # [6, 2, 3, 4, 5]
print("Lista V: {}" .format(V)) # [6, 2, 3, 4, 5]

# Forma "correta" de se fazer uma cópia de uma lista

A = [1, 2, 3, 4, 5] # Lista A
B = A[:] # Nova cópia da lista A
B[0] = 6

print("\n")
print("Lista A: {}" .format(A))
print("Lista B: {}" .format(B))

