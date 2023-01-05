# Programa 6.22 - Exemplo de dicionário com estoque e operações de venda

estoque = {"Tomate": [1000, 2.30],
            "Alface": [500, 0.45],
            "Batata": [2001, 1.20],
            "Feijão": [100, 1.50] }
venda = [["Tomate", 5], ["Batata", 10], ["Alface", 5]]
total = 0
print("Vendas:\n")
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print("Produto: {} - Quantidade: {} x preco - R$ {}, custo = {} " .format(produto, quantidade, preco, custo))
    estoque[produto][0] -= quantidade
    total += custo
    print("Custo total: {}" .format(custo))
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: {}" .format(chave))
        print("Quantidade: {}" .format(dados))
        print("Preço: {}" .format(dados[1]))