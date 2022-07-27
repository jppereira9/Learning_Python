# Programa 6.1 - Cálculo da média

notas = [6, 7, 5, 8, 9] # Criação da lista com 5 notas
soma = 0 # Acumulador
x = 0 # Contador (nesse caso o contador será os índices) 

while x < 5 : # Utilizando um laço para percorrer a lista
    soma += notas[x] # O valor do elemento no índice x é somado ao acumulador
    x += 1 # O contador é incrementado, ou seja, avança para o próximo índice
print("Média: {}" .format(soma / 5)) # A soma dos índices pela quantidade de notas