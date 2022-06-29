'''
- Quando trabalhamos com variáveis, devemos nos lembrar de que o conteúdo de uma variável pode mudar
com o tempo. Isso porque, a cada vez que alteramos o valor de uma variável , o valor anterior é substituido
pelo novo

'''
# Programa 3.1 - Exemplo de sequência de tempo

divida = 0 # Valor inicial de divida igual a 0
compra = 100 # Uma compra de R$ 100,00 foi feita
divida = divida + compra # divida = 0 + 100, ou seja, divida igual a 100
compra = 200 # Uma compra de R$ 200,00 foi feita
divida = compra + divida # divida = 100 + 200, ou seja, divida igual a 300
compra = 300 # Uma compra de R$ 300,00 foi feita
divida = compra + divida # divida = 300 + 300, ou seja, divida igual a 600
print("R$ {:5.2f}" .format(divida)) # R$ 600,00