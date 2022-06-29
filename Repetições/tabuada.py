# Exercicío 5.6 - Altere o programa para exibir os resultados no mesmo formato de uma tabuada: 2 x 1 =2, 2 x 2 = 4,...

n = int(input("Tabuada de: ")) # Recebe qual é a tabuada
x = 1 # x recebe 1
while x <= 10 : # Enquanto x for menor ou igual a n, faça:
    print("{} x {} = {}" .format(x, n, x * n)) # Imprime a tabuada
    x = x + 1 #Incrementa x

