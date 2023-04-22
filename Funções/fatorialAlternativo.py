# Programa 8.4 - Outra forma de calcular o fatorial

# Definindo a função:

def fatorial(n):
    x = 1
    fat = 1
    # Nesse caso a função vai em ordem decrescente
    while x <= n:
        fat *= x
        x += 1
    return fat

# Invocando a função:
print(f'{fatorial(3)}')
print(f'{fatorial(4)}')