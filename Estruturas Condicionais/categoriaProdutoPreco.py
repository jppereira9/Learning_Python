# Programa 4.6 - Categoria x preço

categoria = int(input("Digite a categoria do produto: ")) # Recebendo a categoria do produto
if categoria == 1 : # Categoria 1
    preco = 10
else :
    if categoria == 2: # Categoria 2
        preco  = 18
    else :
        if categoria == 3 : # Categoria 3
            preco = 23
        else :
            if categoria == 4 : # Categoria 4
                preco = 26
            else :
                if categoria == 5 : # Categoria 5
                    preco = 31
                else :
                    print("Categoria invalida, digite um valor entre 1 e 5") # Categoria inválida
print("O preco do produto e = R$ {:5.2f}".format(preco))   


# - Observe que o alinhamento se tornou um grande problema, uma que que tivemos de deslocasr à direita a cada else.

