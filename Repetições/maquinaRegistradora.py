''''
 - Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o
 código do produto e a quantidade comprada. Seu programa deve exibir o total das compras depois que o usuário digitar 0.
 Qualquer código deve gerar a mensagem "Código inválido".

'''
valor_total = 0 # Acumulador

while True :
    codigo = int(input("Digite o código do produto: ")) # Recebendo o código do produto
    if codigo == 0 : # Se o código for igual a 0, então faça:
        break # Termina a execução do programa
    elif codigo == 1 : # Código 1
        qnt_comprada = int(input("Quantidade comprada: ")) # Quantidade comprada
        valor_total = valor_total + (qnt_comprada * 0.5) # valor_total mais a quantidade vezes o preço do produto
    elif codigo == 2 : # Código 2
        qnt_comprada = int(input("Quantidade comprada: ")) # Quantidade comprada
        valor_total = valor_total + (qnt_comprada * 1) # valor_total mais a quantidade vezes o preço do produto
    elif codigo == 3 : # Código 3
        qnt_comprada = int(input("Quantidade comprada: ")) # Quantidade comprada
        valor_total = valor_total + (qnt_comprada * 4) # valor_total mais a quantidade vezes o preço do produto
    elif codigo == 5 : # Código 5
        qnt_comprada = int(input("Quantidade comprada: ")) # Quantidade comprada
        valor_total = valor_total + (qnt_comprada * 7) # valor_total mais a quantidade vezes o preço do produto
    elif codigo == 9 : # Código 9
        qnt_comprada = int(input("Quantidade comprada: ")) # Quantidade comprada
        valor_total = valor_total + (qnt_comprada * 8) # valor_total mais a quantidade vezes o preço do produto
    else : # Se o código for inválido 
        print("Codigo invalido!")
print("\nO total das compras foi: R$ {:5.2f}" .format(valor_total)) # Exibe o valor total das compras