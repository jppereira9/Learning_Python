# Programa 8.15 -  Função imprimeMaior com número indeterminado de parâmetros.

def imprimeMaior (mensagem, *numeros): # Define a função
    maior = None # Maior recebe none
    for e in numeros: # Percore a lista de elementos
        if maior is None or maior < e:
            maior = e
    print (mensagem, maior)

imprimeMaior("Maior: ", 5, 4, 3, 1)
imprimeMaior("Max: ", *[1, 7, 9])
