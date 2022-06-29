'''
 - Exercicío 5.14 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o 
 usuário digite 0. No final da execução, exiba a quantidade de de números digitados, assim como a soma e a média aritmética.

'''
soma = 0 # Acumulador
qnt_numeros = 0 # Contador
media = 0

while True : 
    valor = int(input("Digite um numero a somar ou 0 para sair: ")) # Recebe o valor a ser somado ou para sair do programa
    if valor == 0 : # Se valor for igual a 0, então faça:
        break # Termina a execução do programa
    soma += valor # soma é igual soma mais o valor digitado
    qnt_numeros += 1 # qnt_numeros é incrementado
media = soma / qnt_numeros #Calculo media
# Exibe a quantidade de números digitados, a soma e a média aritmética
print("Quantidade de numeros digitados: {}, soma = {}, media aritmetica = {:5.2f}" . format(qnt_numeros, soma, media))