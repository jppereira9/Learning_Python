'''
 - Exercicío 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês
para os 24 primeiros meses. Escreva o total ganho com juros nesse período

'''
n = 1  # Contador
valor_juros = 0 #Acumulador
deposito_inicial = float(input("Deposito inicial: ")) # Recebendo o depósito inicial
taxa_juros = float(input("Taxa de juros (%): ")) # Taxa de juros ao mês
print("\n")
while n <= 24 : # Enquanto n for menor ou igual a 6, faça
    valor_juros = deposito_inicial * (1 + (taxa_juros / 100)) ** n # Calculando 
    print("{}º mês, R$ {:5.2f}" .format(n, valor_juros - deposito_inicial)) #Exibe o valor que a poupança rendeu em cada mês
    n = n + 1 # Incrementa n
print("\nValor obtido com juros, R$ {:5.2f}" .format(valor_juros)) # Exibe o valor que o juros rendeu durante o período
