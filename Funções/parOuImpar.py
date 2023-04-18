# Vejamos outro exemplo, uma função que retorne verdadeiro ou falso, dependendo se o número é par ou ímpar

def épar(x): # Definindo a função
    return x % 2 == 0

# Invocando a função
print(f'{épar(2)}')
print(f'{épar(3)}')
print(f'{épar(10)}')