# Programa 8.14 -  Função soma com número indeterminado de parâmetros.

def soma (*args): # Definindo a função
    s = 0 # Contador
    for x in args: # Pega o elemento de args e soma ao contador
        s += x
    return s # Retorna a soma

print (soma(1, 2))
print (soma(2))
print (soma(5, 6, 7, 8))
print (soma(9, 10, 20, 30, 40))