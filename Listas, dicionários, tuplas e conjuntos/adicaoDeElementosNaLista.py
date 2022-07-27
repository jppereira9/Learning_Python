# Programa 6.6 - Adição de elementos à lista

L = [] # Lista L(vazia)
while True : # Laço
    n = int(input("Digite um número (0 sai): ")) # Recebe o número digitado
    if n == 0 : # Se o número digitado for igual a 0, o programa é encerrado
        break
    else : # Caso o contrário o número é adicionado à lista
        L.append(n)
x = 0 # Contador
while x < len(L) : # Enquanto x < que o tamanho da lista, imprima cada índice da lista
    print(L[x]) # Imprime o índice x da lista L
    x += 1 # O contador é incrementado