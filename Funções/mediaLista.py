# Vejamos outro exemplo, calculando a média dos valores de uma lista:

# Defininfo a função
def soma(L):
    total = 0
    for x in L:
        total += x
    return total
def media(L):
    return soma(L) / len(L)

# Invocando a função
L = 8, 9, 10, 6, 6, 7
print(f'{media(L)}')