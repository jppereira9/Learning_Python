'''
- Exercicío 4.9 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor
da prestação mensal não pode ser 30% do salário. Calcule o valor da prestação como sendo o valor da casa
a comprar divida pelo número de meses a pagar

'''

valor_casa = int(input("Digite o valor da casa em R$: ")) # Recebendo o valor da casa
salario = float(input("Digite o salario: ")) # Recebendo o valor do salário
qnt_anos = int(input("Digite a quantidade de anos para pagar: ")) # A quantidade de anos para pagar a casa
qnt_meses = qnt_anos * 12 # Convertendo anos para meses
prestacao = valor_casa / qnt_meses # Calculando o valor da prestação

if prestacao > salario * 0.30 : # Caso a mensalidade seja maior que 30% do salário
    print("Emprestimo negado - Valor da mensalidade superior a 30% do salario")
else :
    print("O valor da prestacao = R$ {:5.2f} em {} meses".format(prestacao, qnt_meses)) 


