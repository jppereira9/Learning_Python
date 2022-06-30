# - Exercicío  3.12 - Escreva um programa que calcule o tempo de viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input("Digite a distancia em Km da viagem: ")) # Recebendo a distância da viagem
velocidade_media = int(input("Digite a velocidade media esperada: ")) # Recebendo a velocidade média esperada
tempo_viagem = distancia / velocidade_media # Calculo da velocidade média
print("O tempo esperado de viagem e %d horas" % tempo_viagem)