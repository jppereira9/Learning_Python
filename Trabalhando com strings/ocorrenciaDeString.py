# Exercício 7.1 - Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e impra a posição de inicio
s1 = input("1ª string: ") # Recebe a 1ª string
s2 = input("2ª string: ") # Recebe a 2ª string
print(f'\n\n')

print(f'1ª string: {s1}') # Exibe a 1ª string
print(f'2ª string: {s2}') # Exibe a 2ª string
r = s1.find(s2) # Procura se a 2ª string está dentro da primeira
if  r >= 0: # Se encontra a 2ª string dentro da 1ª, o resultado será maior ou igual a 0, caso contrário, -1
        print(f'Resultado: {s2} encontrado na posição {r} de {s1}') # Imprime a 2ª string a posição na 1ª string
else:
    print(f'Resultado: {s2} não encontrado em {s1}')