# Programa 8.1 - Pesquisa em lista

def pesquise(lista, valor): # Definindo a função
    for x, e in enumerate(lista):
        if e == valor: # Se o valor for encontrado 
            return x # Retorne o valor de sua posição
    return None
    
# Invocando a função
L = [10, 20, 25, 30]
print(f'{pesquise(L, 25)}')
print(f'{pesquise(L, 27)}')
