'''
Exercício 6.13 -  A lista de temperatura de Mons, na Bélgica, for armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

'''

T = [-10, -8, 0, 1, 2, 5, -2, -4] # Lista com a temperatura
maximo = T[0] # maximo recebe o valor do primeiro índice da lista
minimo = T[7] # minimo recebe o valor do último índice da lista 
soma = 0 # Acumulador
for x in T: # Percorrendo a lista
    if x > maximo: # Se o elemento do índice x for maior que máximo
        maximo = x # maximo recebe o valor do índice x
    if x < minimo: # Se o elemento do índice x for menor que minimo
        minimo = x # minimo recebe o valor do índice x
    soma = soma + x # Soma a cada elemento da lista
media = soma / len(T) # Calculando a média de temperatura
print("Maior temperatura: {} cº, menor temperatura: {} cº, temperatura média: {} cº" .format(maximo, minimo, media))