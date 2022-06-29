# Exercicío  5.23 - Escreva um programa que verifique se um númerp é primo ou não

cont_divisores = 0 # Contador de divisores
n = 1 # Contador
numero = int(input("Digite um número: "))
while n <= numero : #Enquanto n for menor ou igual a numero, faça:
    if numero % n  == 0 : # Se a divisão for diferente de 0
        cont_divisores += 1
    n += 1

if cont_divisores == 2 :
    print("\nO número é primo")
else :
    print("\nO número não é primo")

