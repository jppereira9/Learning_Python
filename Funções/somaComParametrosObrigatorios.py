# Podemos combinar parâmetros opcionais com obrigatórios na mesma função

# Programa 8.10 - Função soma com parâmetros obrigatórios e opcioanais
def soma(a, b, imprime = False): # Definindo a função
    s = a + b
    if imprime:
        print(f'{s}')
        return s
print(soma(2, 3))
print(soma(3, 4, True))
print(soma(5, 8, False))
