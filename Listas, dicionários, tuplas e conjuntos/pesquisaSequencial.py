# Programa 6.9 -  Pesquisa sequencial

L = [15, 7, 27, 39] # Lista L
p = int(input("Digite o valor a procurar: ")) # Elemento a ser procurado
achou = False # achou é uma flag
x = 0 # Contador

while x < len(L) : # Vai percorrer a lista
    if L[x] == p : # Compara o elemento presente no índice com o valor digitado
        achou = True # Se os valores forem iguais, achou = True
        break # Encerra a execução do programa
    x += 1 # Incrementa x

if achou == True : # Se achou for True, então o valor foi encontrado
    print("{} achado na posição {}" .format(p, x))
else : # Caso o valor não seja encontrado
    print("{} não encontrado" .format(p))