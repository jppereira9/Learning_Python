# Programa 6.8 - Pilha de pratos

prato = 5 # Pilha com 5 pratos
pilha = list(range(1, prato + 1)) # Criando a pilha com 5 prato começando em 1 e indo até 5
while True :
    print("Existem {} pratos na pilha" .format(prato)) # Quantidade de pratos na pilha
    print("Pilha atual: {}" .format(pilha)) # Pilha atual
    print("\nDigite E para empilhar um novo prato,") # Opções (empilhar, desempilhar ou sair)
    print("ou D para desempilhar. S para sair.")
    operacao = input("\nDigite a operação (E, D ou S): ") # Entrada da operação
    if operacao == "D" : # Desempilhar
        if len(pilha) > 0 : # Se a fila for maior que 0
            lavado = pilha.pop(-1) # O último prato será removido da pilha
            print("Prato {} lavado" .format(lavado)) # Exibe qual prato foi lavado
        else : # Não tem sentido desempilhar uma pilha vazia
            print("Pilha vazia ! Nada para lavar.")
    elif operacao == "E" : # Empilhar
        prato += 1 # Adicionado mais um prato na pilha
        pilha.append(prato) # Adicionando o prato no topo da pilha
    elif operacao == "S" : # Sair do programa
        print("\nVocê escolheu sair")
        break
    else : # Caso da opção seja inválida
        print("Operação inválida! Digite apenas F, A, S!")