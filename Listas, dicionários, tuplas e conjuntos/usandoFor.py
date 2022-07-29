'''
- Python apresenta uma estrutura de repetição especialmente projetada para percorrer listas. A instrução for funciona
de forma parecida a while, mas a cada repetição utiliza um elemento diferente da lista. Exemplo:

'''
L = [8, 9, 15] # Lista L
for x in L : # A instrução começa em L[0] e termina no último índice da lista(L[2])
    print(x) # Imprime cada elemento presente no índice

# Agora realizando a mesma tarefa, porém, com o while
print("\nAgora utilizando o while")
x = 0
while x < len(L) :
    print(L[x])
    x += 1
