# Programa 8.9 - Validação de inteiro usando função:

def faixa_int(pergunta, minimo, maximo): # Definindo a função
    while True: 
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f"Valor inválido. Digite um valor entre {minimo} e {maximo}")
        else:
            return v
        
faixa_int(10, 5, 20)




