# Programa 6.19 - Criação e impressão da lista de compras

compras = [] # Criando a lista compras (inicialmente vazia)
while True:
    produto = input("Produto: ")
    if produto == "Fim" or produto == "FIM" or produto == "fim":
        break
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([produto, quantidade, preco])
    print("\n")
soma = 0.0

print("\n")

for x in compras:
    print(f"{x[0]} - {x[1]} - {x[2]:5.2f} X {x[1] * x[2]:6.2f}")
    soma += x[1] * x[2]
print("Total: {}" .format(soma))