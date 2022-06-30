# - Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_produto =  float(input("Digite o R$ do produto: ")) # Recebendo o valor do produto
desconto = float(input("Digite o desconto: ")) # Recebendo o valor do desconto
preco_desconto = preco_produto - (preco_produto * desconto / 100)
print("O desconto foi de {} % - Preco a pagar R$ {:5.2f}" .format(desconto, preco_desconto)) # Exibindo o desconto e o preço com desconto
