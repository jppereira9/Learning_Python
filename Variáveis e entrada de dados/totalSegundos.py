# Exercicío 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundo do usuário. Calcule o total em segundo

dias = int(input("Digite a quantidade de dias: ")) # Recebendo a quantidade de dias
horas = int(input("Digite a quantidade de horas: ")) # Recebendo a quantidade de horas
segundos = int(input("Digite a quantidade de segundos: ")) # Recebendo a quantidade de segundo
total_segundos = (dias * 24 * 3600) + (horas * 3600) + segundos # Quantidade de dias vezes a quantidade de segundo, mais a quantidade de horas em segundos e soma-se os segundos.
print("{} dias, {} horas e {} segundos, totalizam = {} segundos".format(dias, horas, segundos, total_segundos)) # Exibe o valor do calculo