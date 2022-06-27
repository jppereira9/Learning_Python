
''''
- Exercício 4.2 -  Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h
, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

'''

velocidade = int(input("Digite a velocidade do carro em Km/h: ")) # Recebe a velocidade do veículo
if velocidade <= 80 : # Velocidade dentro do permitido
    print("Velocidade dentro do permitido")
if velocidade > 80 : # Velocidade excedendo 
    valor_multa = (velocidade - 80) * 5
    print("Voce ultrapassou 80 km/h, o valor da multa = R$: %.2f" % valor_multa)
