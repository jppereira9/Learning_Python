# Exercicío 3.10 - Faça um programa que calcule o aumento de um salário . Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o salario R$: ")) # Recebe o salário
aumento = int(input("Digite o valor do aumento: ")) # Recebe o aumento
novo_salario = salario + (salario * aumento / 100) # Calculo do salário com aumento
print("Novo salario = {}, aumento de {}%" .format(novo_salario, aumento)) # Exibe o novo salário e o aumento