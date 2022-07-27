# Programa 6.2 - Cálculo da média com notas digitadas

notas = [0, 0, 0, 0, 0] # Criando uma lista com 5 elementos, inicialmente cada elemento é 0
soma = 0 # Acumulador
x = 0 # Contador

while x < 5 : # Laço para preencher as 5 notas
    notas[x] = float(input("Nota {}: " .format(x))) # Naquele índice será armazenado o valor digitado
    soma += notas[x] # O valor das notas é soma
    x += 1 # x é incrementado
print("A média das notas digitadas foi:{:6.2f}" .format(soma / 5)) # Exibindo o resultado