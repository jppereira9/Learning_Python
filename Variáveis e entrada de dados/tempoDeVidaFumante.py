'''
 - Exercicío 3.15: Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade 
de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro
, e calcule quantos dias um fumante perderá. Exiba o total em dias.

'''
anos_fumando = int(input("Fuma durante quantos anos? ")) # Anos fumando
cigarros_por_dia = int(input("Fuma quantos cigarro por dia? ")) # Cigarros por dia
tempo_perdido = (anos_fumando * 365 * cigarros_por_dia) / 1400
print("Fumando {} cigarros por dia, durante {} anos, voce perdeu{:5.0f} dias de vida" .format(cigarros_por_dia, anos_fumando, tempo_perdido))