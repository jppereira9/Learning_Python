# Poderíamos também ter definido a função média como:

# Definindo a função:
def media(L):
    total = 0
    for x in L:
        total += x
    return total / len(L)

# Invocando a função:
L = [10, 9, 7, 8, 9, 10, 8]
print(f'{media(L)}')

