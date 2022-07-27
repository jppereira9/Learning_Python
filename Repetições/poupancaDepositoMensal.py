'''
 - Exercicío 5.12 - Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
 Esse valor será depositdado no inicio de cada mês, e você deve considerá-lo para o calculo de juros no período.

'''

n = 1  # Contador
valor_juros = 0 #Acumulador
deposito_inicial = float(input("Deposito inicial R$: ")) # Recebendo o depósito inicial
taxa_juros = float(input("Taxa de juros (%): ")) # Taxa de juros ao mês
deposito_mensal = float(input("Valor do depósito mensal - R$: ")) # Recebe deposito mensal
valor_juros = deposito_inicial 

while n <= 24 : # Enquanto n for menor ou igual a 6, faça:
    valor_juros += (valor_juros * (taxa_juros / 100)) + deposito_mensal # Calculando do juros composto
    print("Mês - {}, rendimento - R$ {:5.2f}" .format(n, valor_juros)) #Exibe o mês e o rendimento do mês
    n += 1 # Incrementa n
print("\nValor final obtido - R$ {:5.2f}" .format(valor_juros)) # Exibe o valor final obtido com juros