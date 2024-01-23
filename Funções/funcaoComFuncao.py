# Programa 8.13 - Configuração de funções com funções

def imprime_lista(L, fimpressao, fcondicao): # Função imprime_lista
    for e in L:
        if fcondicao(e):
            fimpressao(e)

def imprime_elemento(e): # Função imprime elemento
    print(f"Valor: {e}") 

def epar(x): # Função é par
    return x % 2 == 0

def eimpar(x): # Função é impar
    return not epar(x)

L = [1, 7, 9, 2, 11, 0] # Definindo a lista

imprime_lista(L, imprime_elemento, epar) # Chamada de função