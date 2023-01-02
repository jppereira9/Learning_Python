# Programa 6.11 - Verificação do maior valor

L = [1, 7, 2, 4] # Lista com 4 elementos
maximo = L[0] # Máximo recebe o valor do índice 0
for x in L: # Percorre a lista
    if x > maximo: # Se o elemento na posição x for maior que máximo
        maximo = x # maximo recebe o elemento na posição x
print(maximo) # Exibe o maior valor da lista


