# Programa 8.7 - Função recursiva de Fibonacci

def fibonacci(n): # Definindo a função
    if n <= 1: # Casos base
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))
print(fibonacci(7))