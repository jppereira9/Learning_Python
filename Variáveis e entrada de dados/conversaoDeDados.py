'''
 - Se digitarmos um número, o resultado sempre será uma string, para resolver isso precisamos usar a função int 
ou a função float.

'''
anos = int(input("Anos de servicos: ")) # Recebe a quantidade de anos, convertendo para int
valor_por_ano = float(input("Valor por ano: ")) # Recebe o valor por ano, convertendo em float
bonus = anos * valor_por_ano # Calcula o bônus
print("Bonus de R$ %.2f" % bonus) # Imprime o bônus