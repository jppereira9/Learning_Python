'''
 - Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 km, e R$ 0,45 para viagens mais longas

'''
distancia_viagem = int(input("Digite a distanca em Km: ")) # Recebendo a distância em Km

if distancia_viagem <= 200 : # Se a viagem for menor até 200 km
    preco_pagar = distancia_viagem * 0.50 # Até 200 km, o preço do Km é R$ 0,50
    print("Para uma viagem de {:5.2f} Km, o valor = R$ {:5.2f}".format(distancia_viagem, preco_pagar)) # Distancia de total a pagar
else :
    preco_pagar = distancia_viagem * 0.45   
    print("Para uma viagem de {:5.2f} Km, o valor = R$ {:5.2f}" .format(distancia_viagem, preco_pagar)) # Distancia de total a pagars 