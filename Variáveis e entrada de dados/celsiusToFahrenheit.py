# Exercicío 3.13 - Escreva um programa que converta uma temperatura digitada em Cº em Fº.

from ctypes.wintypes import INT


celsius = float(input("Digite a temperatura em C: ")) # Recebendo a temperatura em graus Celsius
fahrenheit = ((9 * celsius) / 5) + 32 # Convertendo a temperatura
print("A temperatura convertida = %.2f F" % fahrenheit) # Exibindo a temperatura convertida