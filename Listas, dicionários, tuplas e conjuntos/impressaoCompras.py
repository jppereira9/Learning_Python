# Programa 6.18 - Impressão de compras

produto1 = ["Maçã", 10, 0.30] # Lista produto1
produto2 = ["Pera", 5, 0.75] # Lista produto2
produto3 = ["Kiwi", 4, 0.98] # Lista produto2
compras = [produto1, produto2, produto3] # compras é uma lista que contém 3 listas

for x in compras:
    print("Produto - {[0]}" .format(x))
    print("Quantidade - {[1]}" .format(x))
    print("Preço - {[2]}" .format(x))
    print("\n")