'''
- Exercicío 4.10 - Escreva um program que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a
quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule
o preco a pagar de acordo com a tabela (tabela no livro).

'''

qnt_kwh = int(input("Digite a quantidade de kWh consumidos: ")) # Recebendo a quantidade de kWh consumidos
tipo_instalacao = input("Digite o tipo de instalacao: ") # Recebendo o tipo de instalação

if tipo_instalacao == "R" or tipo_instalacao == 'r' : # Residencial
    if qnt_kwh <= 500 : # Quantidade de kWh consumidos
        preco = 0.40 # Preco do kWh
        print("Tipo de residencia = {}, valor a pagar R$ {:5.2f}".format(tipo_instalacao, qnt_kwh * preco))
    else :
        preco = 0.65 # Preco do kWh
        print("Tipo de residencia = {}, valor a pagar R$ {:5.2f}".format(tipo_instalacao, qnt_kwh * preco))

elif tipo_instalacao == "C" or tipo_instalacao == 'c' : # Comercial
    if qnt_kwh <= 1000 : # Quantidade de kWh consumidos
        preco = 0.55 # Preco do kWh
        print("Tipo de residencia = {}, valor a pagar R$ {:5.2f}".format(tipo_instalacao, qnt_kwh * preco))
    else :
        preco = 0.60
        print("Tipo de residencia = {}, valor a pagar R$ {:5.2f}".format(tipo_instalacao, qnt_kwh * preco))

elif tipo_instalacao == "I" or tipo_instalacao == 'i' : # Industrial
    if qnt_kwh <= 5000 : # Quantidade de kWh consumidos
        preco = 0.55 # Preco do kWh
        print("Tipo de residencia = {}, valor a pagar R$ {:5.2f}".format(tipo_instalacao, qnt_kwh * preco))
    else : 
       preco = 0.60 # Preco do kWh
       print("Tipo de residencia = {}, valor a pagar R$ {:5.2f}".format(tipo_instalacao, qnt_kwh * preco))
else : 
    print("Tipo invalido de instalacao, tente novamente")

