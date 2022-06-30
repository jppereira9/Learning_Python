# - Exercicío 3.8 - Escreva um programa que leia um valor em metros e o exiba convertendo em milímetros

metros = int(input("Digite o valor em metros: ")) # Recebe a quantidade em metros 
milimetros = metros * 1000 # Calcula a quantidade em milimetros (cada metro tem mil milimetros)
print("{} metros, sao {} milimetros" .format(metros, milimetros)) #Exibe a quantidade de metros em milimetros