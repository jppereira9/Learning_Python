# Programa 8.12 - Funções com parâmetros

def soma(a, b): # Função soma
    return a + b

def subtracao(a, b): # Função subtração
    return a - b

def imprime(a, b, foper): # Função imrpime
    print(foper(a, b))

imprime(5, 4, soma) # Chamada de função

imprime(10, 1, subtracao) # Chamada de função

 
