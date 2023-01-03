# Programa 6.14 - Lendo e imprimindo uma lista de compras
compras = [] # Criando uma lista vazia
while True: # Laço
    produto = input("Produto: ") # Recebe o nome do produto
    if produto == "fim" or produto == "FIM" or produto == "Fim": # Encerra o laço caso seja digitado Fim
        break
    else: # Adiciona o produto na lista
        compras.append(produto)
print("\n----- Lista de compras -----")
for x, compras in enumerate(compras): # Utiliza o enumerate 
    print("{} - {}" .format(x + 1, compras)) # Imprime o nome do produto na lista
