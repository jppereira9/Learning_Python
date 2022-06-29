# Vamos escrever um programa de forma que o último número a imprimir seja informado pelo usuário

fim = int(input("Digite o ultimo numero a imprimir: ")) # Recebe o último número da contagem
x = 1 # x recebe 1
while x <= fim : # Enquanto x for menor ou igual ao número digitado, faça:
    print(x) # Imprime o valor de x
    x = x + 1 # O valor de x é incrementado
