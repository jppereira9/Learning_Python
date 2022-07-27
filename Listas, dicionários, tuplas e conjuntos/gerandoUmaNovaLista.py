# Exercício 6.2 - Faça um programa que leia duas lista e que gere uma terceita com os elementos das duas primeiras

x = 0 # Contador
y = 0 # Contador

L1 = [23, 65, 33, 52, 46, 89, 91, 109] # Lista L1
L2 = [1, 127, 309,678, 10001] # Lista L2
nova_lista = [] # Lista voa_lista que vai receber os elementos de L1 e L2
while x < len(L1) : # Percorrendo a lista L1
    nova_lista.append(L1[x]) # Adicionando os elementos da lista L1 à nova_lista
    x += 1 # Incrementa o contador
while y < len(L2) : # Percorrendo a lista L2
    nova_lista.append(L2[y]) # Adicionando os elementos da lista L2 à nova_lista
    y += 1 # Incrementa o contador
print(nova_lista) # Imprime a 3ª lista