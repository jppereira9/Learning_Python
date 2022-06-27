# Programa 4.5 - Conta de telefone com três faixas de preço

minutos = int(input("Quantos minutos voce utilizou esse mes: ")) # Recebe os minustos utilizados
if minutos < 200 : # Se a quantidade for menor que 200
    preco = 0.20 
else :
    if minutos < 400 : # Se a quantidade for entre 200 e 400
        preco = 0.18
    else :
        preco = 0.15
print("Voce vai pagar este mes - R$ {:5.2f}".format(minutos * preco)) #Valor a ser pago

