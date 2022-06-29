# Modifique 0 programa anterior de forma que o usuário também digite o inicio e o fima da tabuada

inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

while inicio <= fim :
    print("{} x {} = {}" .format(inicio, fim, inicio * fim))
    inicio = inicio + 1
 
