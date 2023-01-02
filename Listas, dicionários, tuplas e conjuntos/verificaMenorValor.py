# Programa 6.12 - Verificação do menor valor

L = [1, 7, 2, 4] # Lista com 4 elementos
minimo = L[0] # minimo recebe o valor do índice 0
for x in L: # Percorre a lista
    if x < minimo: # Se o elemento na posição x for maior que máximo
        minimo = x # minimo recebe o elemento na posição x
print(minimo) # Exibe o maior valor da lista


