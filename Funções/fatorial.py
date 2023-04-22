# Programa 8.3 -  Cálculo de fatorial

# Definindo a função
def fatorial(n):
    fat = 1
    # Nesse caso a função vai em ordem crescente
    while n > 1:
        fat *= n
        n -= 1
    return fat

# Invocando a função:
print(f'{fatorial(3)}')
print(f'{fatorial(4)}')