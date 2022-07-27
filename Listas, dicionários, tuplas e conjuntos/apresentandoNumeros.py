from pickle import TRUE


numeros = [0, 0, 0, 0, 0]
x = 0

while x < 5 :
    numeros[x] = int(input("Número {}: " .format(x + 1)))
    x += 1

print("\n")

while True :
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0 :
        break 
    else :
        print("Você escolheu o número: {:1.0f}" . format(numeros[escolhido - 1]))
    print("\n")