'''
- Remoção de elementos da lista: Como o tamanho da lista pode variar, permitindo a adição de novos elementos,
podemos também retirar elementos da lista, ou mesmo, todos eles. Para isso, utilizamos a função del:

'''
L = ["a", "b", "c"] # Lista L = a, b, c
print(L)

del L[1] # Removendo o elemento do índice 1(b)
print(L)

del L[0] # Removendo o elemento do índice 0(a)
print(L)
print("\n")

# Podemos também apagar fatias inteiras de uma só vez:

L = list(range(101)) # Criando lista com 101 elementos começando em 0

'''
- A dunção range gera uma sequência de elementos, mas a cada chamada, sendo o que chamamos de generator. A função
list é utilizada para transformar o resultado dessa função em uma lista.

'''
print(L)
print("\n")

del L[1:99] # Apaga os valores do índice 1 até o índce 99
print(L)