# Programa 6.13 - Controle da utilização de sala de um cinema

lugares_vagos = [10, 2, 1, 3, 0] # Lugares vagos por vaga
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input("Quantos lugares você deseja, {} vaga: " .format(lugares_vagos[sala - 1])))
    if lugares > lugares_vagos[sala - 1]:
        print("Esse números de lugares não está disponível")
    elif lugares < 0:
        print("Número inválido")
    else:
        lugares_vagos[sala - 1] -+ lugares
        print("{} lugares vendidos" .format(lugares))
print("Utilização de salas")
for x, l in enumerate (lugares_vagos):
    print("Sala {} - {} lugar(es) vazio(s)" .format(x + 1, l,))