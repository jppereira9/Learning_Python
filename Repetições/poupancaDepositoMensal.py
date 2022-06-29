'''
 - Exercicío 5.12 - Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
 Esse valor será depositdado no inicio de cada mês, e você deve considerá-lo para o calculo de juros no período.

'''
n = 1  # Contador
valor_juros = 0 #Acumulador
deposito_inicial = float(input("Deposito inicial: ")) # Recebendo o depósito inicial
taxa_juros = float(input("Taxa de juros: ")) # Taxa de juros ao mês

while n <= 24 : # Enquanto n for menor ou igual a 6, faça
    deposito_mensal = float(input("\nValor do deposito - R$: ")) # Calcula do juros composto
    valor_juros = (deposito_mensal + deposito_inicial) * (1 + (taxa_juros / 100)) ** n # Calculando 
    print("{}º mes, R$ {:5.2f}" .format(n, valor_juros - deposito_inicial)) #Exibe o valor que a poupança rendeu em cada mês
    n = n + 1 # Incrementa n
print("\nValor obtido com juros, R$ {:5.2f}" .format(valor_juros)) # Exibe o valor que o juros rendeu durante o período
