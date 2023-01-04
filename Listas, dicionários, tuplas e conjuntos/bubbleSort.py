# Programa 6.20 - Ordenação pelo método de bolhas

L = [ 7, 4, 3, 12, 8] # Lista
fim = 5 # Quantidade de elementos na lista
while fim > 1: # Para realizar a ordenação é necessário pelo menos 2 elementos
    trocou = False # Uma flag para indicar se houve troca ou não
    x = 0 # x é utilizado como índice
    while x < (fim - 1): # A condição de saída é que x seja o penúltimo elemento
        if L[x] > L[x + 1]: # Compara se o valor da posição corrente é maior que a próxima posição
            trocou = True # Se o elemento atual é maior que o próximo elemento
            temp = L[x] # Nesse caso o valor de L[x] é armazenado em temp
            L[x] = L[x + 1] # A posição atual recebe o valor da posição seguinte
            L[x + 1] = temp # A posição sub-sequente recebe o valor da posição anteior
        x += 1 # Avança no índice da lista
    if not trocou: # VVerifica se a lista está ordenada
        break
        fim -= 1
for x in L:
    print(x)