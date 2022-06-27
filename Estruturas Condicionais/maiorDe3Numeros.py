# Exercicío 4.3 - Escreva um rpograma que leia três números e que imrpima o maior e o menor.

n1 = int(input("Primeiro numero: ")) # Recebendo o primeiro número:
n2 = int(input("Segundo numero: ")) # Recebendo o segundo número
n3 = int(input("Terceiro numero: ")) # Recebendo o terceiro número

#Inicializando variáveis


if n1 > n2 and n1 > n3 : # n1 maior
    maior = n1 # Armazena o maior valor

if n2 > n1 and n2 > n3 : # n2 maior
    maior = n2 # Armazena o maior valor

if n3 > n1 and n3 > n2 : # n3 maior
    maior = n3 # Armazena o maior valor

if n1 < maior and n1 < n3: # n1 menor
    menor = n1 # Armazena o menor valor

if n2 < n1 and n2 < n3: # n2 menor
    menor = n2 # Armazena o menor valor

if n3 < n1 and n3 < n2 : # n3 menor
    menor = n3 # Armazena o menor valor
print("Maior = {} | Menor = {}".format(maior, menor))

