# Programa 8.22 - Função retângulo com parâmetro obrigatórios e opcionais

def retangulo(largura, altura, caractere = "*"): # Função retângulo
    linha =  caractere * largura
    for i in range(altura):
        print(linha)

retangulo(3, 4) # Chamada da função
print("\n")

retangulo(largura = 3, altura = 4) # Chamada da função
print("\n") # Chamada da função

retangulo(altura = 4, largura = 3) # Chamada da função
print("\n")

retangulo(caractere = "-", altura = 4, largura = 3) # Chamada da função