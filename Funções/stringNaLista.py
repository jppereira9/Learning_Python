'''
Exerício 8.12 - Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada
com os elementos da listam também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro
da lista, e falso, caso o contrário

'''

def stringNaLista(string, lista): # Definindo a função
    for x in lista: # Varredura da lista
        if string in lista: # Verifica se a string está na lista
            return True
        else:
            return False
        
L = ["Banana", "Gato", "Computador", "Abacaxi", "Carro"] # Criando a lista

print(stringNaLista("Banana", L)) # True
print(stringNaLista("Avião", L)) # False