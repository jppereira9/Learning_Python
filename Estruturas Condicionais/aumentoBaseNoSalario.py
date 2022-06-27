'''
Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superior a R$ 1250,00, calcule um aumento de 10%. Para inferiores de 15%

'''
salario = float(input("Digite o salario: ")) # Recebendo o salario
if salario > 1250 : # Salário maior que R$ 1250,00
    aumento = salario * 0.1 # Aumento de 10%
    print("Salario de R$ {:5.2f}, aumento de R$ {:5.2f}" .format(salario, aumento)) # Exibindo salário e valor do aumento

if salario < 1250 : # Salário menor que R$ 1250,00
    aumento = salario * 0.15 # Aumento de 15%
    print("Salario de R$ {:5.2f}, aumento de R$ {:5.2f}" .format(salario, aumento)) # Exibindo salário e valor do aumento