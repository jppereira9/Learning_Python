'''
- Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular
soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba a operação solicitada

'''
n1 = int(input("Digite o primeiro numero: ")) # Recebendo o primeiro número
n2 = int(input("Digite o segundo numero: ")) # Recebendo o segundo número

opcao = int(input("Qual operacao deseja realizar (1, 2, 3 ou 4): ")) # Recebendo qual a opção desejada
if opcao == 1 : # Operação de soma
    operacao = n1 + n2
    print("O resultado da operação = %d" % operacao)
elif opcao == 2 : # Operação de substração
    operacao = n1 - n2
    print("O resultado da operação = %d" % operacao)
elif opcao == 3 : # Operação de multiplicação
    operacao = n1 * n2
    print("O resultado da operação = %d" % operacao)
elif opcao == 4 : # Operação de divisão
    if n2 == 0: # n2 precisa ser diferente de 0!
        print("Impossivel dividir por 0")
    else :
        operacao = n1 / n2
        print("O resultado da operação = %.2f" % operacao)
else :
    print("Opcao invalida, digite um numero entre 1 e 5")

