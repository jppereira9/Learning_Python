# Em python definiríamos a função recursiva para cálculo do fatorial como:

# Programa 8.5 - Função fatorial recursiva

def fatorial(n): # Definindo a função
    print(f'Calculando o fatorial de {n}')
    if n == 0 or n == 1: # Se n = 1 ou n =0, fatorial é igual a 1 - Caso Base
        print(f'Fatorial de {n} = 1')
        return 1 # Retornando 1
    else:
        fat = n * fatorial(n - 1) # Se fatorial for diferente de 0 ou 1, retorne o número menos 1
        print(f'Fatorial de {n} = {fat}')
        return fat # Retornando o fatorial de n
fatorial(4)