'''
- Uma das estruturas de repetição do Python é o while, que repete um bloco enquanto a condição for verdadeira. Seu formato
é apresentado a seguir, em que condição é uma expressão lógica, e bloco representa as linhas de programa a repetir as
linhas de programa a repetir o resultado da condição for verdadeiro.

while <condição> :
    bloco

'''
# Para resolver o problema de escrever três números utilizando o while, escreveríamos o programa:

x = 1 # Inicializando a variável x com 1
while x <= 3 : #Enqunato x for menor ou igual a 3, faça:
    print(x) # Imprime o valor de x
    x = x + 1 # Incrementa o valor da variável x

print("\n")

# Exercicío 5.1 - Modifique o programa para exibir os números de 1 a 100
print("Numeros de 1 a 100: ")
x = 1 # Inicializando a variável x com 1
while x <= 100 : #Enqunato x for menor ou igual a 100, faça:
    print(x) # Imprime o valor de x
    x = x + 1 # Incrementa o valor da variável x
    print("\n")

# Exercicío 5.2 - Modifique o programa para exibir os números de 50 a 100
print("Numeros de 50 a 100: ")
x = 50 # Inicializando a variável x com 50
while x <= 100 : #Enqunato x for menor ou igual a 100, faça:
    print(x) # Imprime o valor de x
    x = x + 1 # Incrementa o valor da variável x