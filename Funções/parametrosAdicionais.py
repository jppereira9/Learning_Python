'''
Nem sempre precisaremos passar todos os parâmetros para uma função, preferindo utilizar um valor
previamente escolhido por padrão

Vejamos um exemplo de uma função que imprime uma barra na tela:

'''
def barra(): # Definindo a função
    print(f'*' * 40) # Imprime 40x o *
barra() # Invocando a função

def barra_2(n = 40, caractere = "*"): # Definindo a função
    print(f'{caractere}' * n) # Imprime o caractere e a quantidade de vezes
barra_2(10) # Imprime 10 vezes *
barra_2(10, "-") # Imrpime 10 vezes o caractere -
