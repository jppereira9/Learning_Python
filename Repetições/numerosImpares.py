# Exercício 5.4 - Modifique o programa anterior para imprimir de 1 até o número digitado plelo usuário, mas, dessa vez, apenas os númeprs ímpares

fim = int(input("Digite o ultimo numero a imprimir: ")) # Recebe o último número da contagem
x = 1 # x recebe 1
while x <= fim : # Enquanto x for menor ou igual ao número digitado, faça:
    if x % 2 != 0 : # Se o número não for impar
        print(x) # Imprime o valor de x
    x = x + 1 # O valor de x é incrementado

print("\nJeito alternativo: ")
fim = int(input("Digite o ultimo numero a imprimir: ")) # Recebe o último número da contagem
x = 1 # x recebe 1
while x <= fim : # Enquanto x for menor ou igual ao número digitado, faça:
    print(x) # Imprime o valor de x
    x = x + 2 # O valor de x é incrementado de 2 em 2
