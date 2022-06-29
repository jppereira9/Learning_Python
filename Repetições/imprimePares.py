# Recebe o últmo número a ser impresso e o programa verifica se o número é par e o imprime em caso positivo

fim = int(input("Digite o ultimo numero a imprimir: ")) # Recebe o último número da contagem
x = 0 # x recebe 0
while x <= fim : # Enquanto x for menor ou igual ao número digitado, faça:
    if x % 2 == 0 : # Verifica se x é multiplo de 2, ou seja, primo
        print(x) # Se for primo, imprime o numero
    x = x + 1 # Incrementa x

print("\nJeito alternativo")
fim = int(input("Digite o ultimo numeor a imprimir: ")) # Recebe o último número da contagem
x = 0 # x recebe 0
while x <= fim : # Enquanto x for menor ou igual ao número digitado, faça:
    print(x) # Se for primo, imprime o numero
    x = x + 2  # Incrementa x de 2 em 2