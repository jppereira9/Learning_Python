'''
- elif - Python apresenta uma solução muito interessante ao problema de múltiplos ifs aninhados. A cláusula elif
substitui um par de else if, mas sem criar outro nível de estrutura, evitando deslocamentos desnecessários à direita

'''
# Programa 4.6 - Categoria x preço, usando elif

categoria = int(input("Digite a categoria do produto: ")) # Recebendo a categoria do produto
if categoria == 1 : # Categoria 1
    preco = 10
elif categoria == 2: # Categoria 2
    preco  = 18
elif categoria == 3 : # Categoria 3
        preco = 23
elif categoria == 4 : # Categoria 4
        preco = 26
elif categoria == 5 : # Categoria 5
         preco = 31
else :
    print("Categoria invalida, digite um valor entre 1 e 5") # Categoria inválida
    preco = 0
print("O preco do produto e = R$ {:5.2f}".format(preco))   
