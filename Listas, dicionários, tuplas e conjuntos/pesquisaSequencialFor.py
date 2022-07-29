# Pesquisa sequencial utilizando o for

L = [7, 9, 10, 12] # Lista L
p = int(input("Digite um número a pesquisar: ")) # Elemento a ser procurado

for x in L : # Percorrer todos os elementos da lista
    if x == p : # Compara o valor pesquisado com o elemento da lista
        print("Elemento encontrado!") # Exibe a mensagem se encontrou o valor
        break # Interrompe a execução do programa
else : # Caso a lista toda tenha sido percorrida e o elemento não tenha sido encontrado
    print("Elemento não encontrado!")
