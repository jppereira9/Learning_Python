# Programa 6.15 - Impressão de uma lista de stringsm letra a letra

L = ["Maçãs", "Peras", "Kiwis"] # Criação da lista com 3 strings
for x in L: # O laço percorre a lista
    for letra in x: # O laço interno percorrerá cada letra dentro da string
        print(letra) # Imprime a letra da palvra corrente