''''
 - Exercicío  5.22 - Escreva um programa que exiba uma lista de opções(menu): adição, subtraçãom divisãi, multiplicação
 e sair. Imprima a tabuada da operação escolhida. Repita até que a opção sáida seja escolhida.

'''
print("------- Opções -------")
print("Adição")
print("Subtração")
print("Divisão")
print("Multiplicação")
print("Sair")

while True :
    opcao = input("\nDigite uma opção: ") # Recebe a opção
    print("\n")
    if opcao == "SAIR" or opcao == "Sair" or opcao == "sair" : # Sai do programa, encerrando sua execução
        break
    elif opcao == "ADIÇÃO" or opcao == "Adição" or opcao == "adição" : # Tabuada de adição
        tabuada = 1 # Contador
        while tabuada <= 10 :
            numero = 1 # Contador
            while numero <= 10 :
                print("{} + {} = {:1.0f}" . format(tabuada, numero, tabuada + numero))
                numero += 1 # Incrementa numero
            tabuada += 1 # Incrementa tabuada
            print("\n")
    elif opcao == "SUBTRAÇÃO" or opcao == "Subtração" or opcao == "subtração" : # Tabuada de subtração
        tabuada = 1 # Contador
        while tabuada <= 10 :
            numero = 1 # Contador
            while numero <= 10 :
                print("{} - {} = {:1.0f}" . format(tabuada, numero, tabuada - numero))
                numero += 1 # Incrementa numero
            tabuada += 1 # Incrementa tabuada
            print("\n")
    elif opcao == "DIVISÃO" or opcao == "Divisão" or opcao == "divisão" : # Tabuada de divisão
        tabuada = 1 # Contador
        while tabuada <= 10 :
            numero = 1 # Contador
            while numero <= 10 :
                print("{} / {} = {:1.0f}" . format(tabuada, numero, tabuada / numero))
                numero += 1 # Incrementa numero
            tabuada += 1 # Incrementa tabuada
            print("\n")
    elif opcao == "MULTIPLICAÇÃO" or opcao == "Multiplicação" or opcao == "multiplicação" : # Tabuada de multiplicação
        tabuada = 1 # Contador
        while tabuada <= 10 :
            numero = 1 # Contador
            while numero <= 10 :
                print("{} x {} = {:1.0f}" . format(tabuada, numero, tabuada * numero))
                numero += 1 # Incrementa numero
            tabuada += 1 # Incrementa tabuada
            print("\n")
    else :
        print("Opção inválida")

    tabuada = 1
    numero = 1
  
