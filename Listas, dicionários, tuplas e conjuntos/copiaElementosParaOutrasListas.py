# Programa 6.12 - Cópia de elementos para outras listas

v = [9, 8, 7, 12, 0, 13, 21] # Criação da lista com os elementos
P = [] # Lista para os números pares
I = [] # Lista para os números ímpares

for x in v: # Percorrendo os elementos da lista
    if x % 2 == 0: # Verificando se o número é par
        P.append(x) # Caso o número seja par, ele é adicionado na lista P
    else:
        I.append(x) # Caso o númerp seja impar, ele é adicionado na lista I
print("Números pares: {}" .format(P)) # Imprimindo a lista de números pares
print("Números ímpares: {}" .format(I)) # Imprimindo a lista de número impares