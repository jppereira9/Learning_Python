# Programa 6.21 - Obtenção do preço com um dicionário

tabela = {"Alface": 0.45, "Batata": 1.20, "Tomate": 2.30, "Feijão": 1.50} # Criação do dicionário
while True: # Laço de repetição
    produto = input("Digite o bome do produto, fim para terminar: ") # Produto recebe o produto a ser pesquisado
    if produto == "fim" or produto == "FIM" or produto == "Fim": # Se o produto for igual a fim, se encerra o programa
        break
    if produto in tabela: # Verifica se a chave contida em produto está no dicionário
        print("R$ {}" .format(tabela[produto])) # Exibe o preço do produto
    else:
        print("Produto não encontrado") # Caso o produto não esteja na lista

