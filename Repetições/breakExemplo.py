# Vejamos um exemplo da leitura de valores até que digitemos 0:

soma = 0 # Contador
while True :
    valor = int(input("Digite um numero a somar ou 0 para sair: "))
    if valor == 0 : # Se o valor for igual a 0, então:
        break # Termina a execução do programa
    soma += valor # soma igual soma mais o valor digitado
print("A soma = %d" % soma)