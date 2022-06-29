# Vejamos um programa que calculea soma de 10 números. Nesse caso soma é o acumulador e n é um contador.

n = 1 #Contador
soma = 0 # Acumulador

while n <= 10 :  # Enquanto n for menor ou igual a 10, faça:
    x = int(input("Digite o {} valor: " .format(n))) # Recebe o valor a ser somado
    soma = soma + x # O valor anterior do acumulador mais o novo valor
    n = n + 1 # Contador é incrementado
print("\nSoma = {}" .format(soma)) # Exibe a soma