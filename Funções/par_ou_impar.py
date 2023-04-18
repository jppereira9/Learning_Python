# Imagine agora que precisamos definir uma função para retornar a palavra par ou ímpar. 

def épar(x): # Definindo a função
    return x % 2 == 0
def par_ou_impar(x): # Definindo a função
    if épar(x):
        return "Par"
    else:
        return "Ímpar"

# Invocando a função
print(f'{par_ou_impar(4)}')
print(f'{par_ou_impar(5)}')