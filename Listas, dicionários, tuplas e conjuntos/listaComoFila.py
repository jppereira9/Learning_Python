# Programa 6.7 - Simulação de uma fila de banco

ultimo = 10 # 10 pessoas na fila
fila = list(range(1, ultimo + 1)) # A fila começa em 1 e vai até 10 + 1 para a fila comecar em 1 e terminar em 10
while True :
    print("Existem {} clientes na fila" .format(len(fila))) # Quantidade de pessoas na fila
    print("\nFila atual: {}" .format(fila)) # "Clientes na fila"
    print("\nDigite F para adicionar um cliente ao fim da fila,") # Inserir ou atender cliente
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("\nOperação (F, A, S): ") # Entrada da operação
    if operacao == "A" : # Atendimento do cliente
        if len(fila) > 0 : # Se a fila não for vazia
            atendido  = fila.pop(0) # O cliente que foi atendido é o primeiro cliente da fila
            print("\nCliente {} atendido" .format(atendido)) # Exibe qual o cliente que foi atendido
        else:
            print("Fila vazia! Ninguém para atender") # Não há sentido atender alguém de uma fila vazia
    elif operacao == "F" : # Cliente chega para ser atendido
            ultimo += 1 # Incrementa um novo cliente na fila
            fila.append(ultimo) # O tamanho da fila foi aumentado e o novo cliente está no fim da fila
    elif operacao == "S" : # Sair do programa
        print("\nVocê escolheu sair")
        break
    else : # Caso da opção seja inválida
        print("Operação inválida! Digite apenas F, A, S!")