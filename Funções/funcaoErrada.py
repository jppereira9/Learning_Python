# Programa 8.2 - Como não escrever uma função

# Definindo a função
def soma(L):
    total = 0
    x = 0
    while x < 5:
        total += L[x]
        x += 1
    return total

# Criando a lista
L = [1, 7, 2, 9, 15]
# Invocando a função
print(f'{soma(L)}') # Funciona corretamente
print(f'{soma([7, 9, 12, 3, 100, 20, 4])}') # Não funcioona corretamente, pois a função calcula a soma de 5 números e não de mais
