# Vejamos um programa que calcula a média de cinco números digitados pelo usuário.

n = 1 # Contador
soma = 0 # Acumulador
while n <= 5 : # Enquanto n for menor ou igual a 5, faça:
    x = int(input("{} - Digite o numero: " .format(n))) # Recebe o valor a ser somado
    soma = soma + x # O valor anterior do acumulador mais o novo valor
    n = n + 1 # Contador é incrementado

media = soma / 5 # Calculo da média
print("\nA media dos 5 numeros = {:5.2f}" .format(media)) # Exibe a media
