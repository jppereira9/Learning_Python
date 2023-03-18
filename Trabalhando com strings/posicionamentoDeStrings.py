'''
Python também traz métodos que ajudam a apresentar de formas mais interessantes. Vejamos
o método center, que centraliza a string em um número de posições passado como parâmetro,
preenchendo com espaços à direita e à esquerda até que a string esteja centralizada

'''
s = "Tigre"
print("X" + s.center(10) + "X")
print("X" + s.center(10, ".") + "X")

# Se o que você deseja é apenas completar a string com espaços à esquerda, pode utilizar o método ljust ou rjust
s2 = "Batata"
print(s2.ljust(20, "."))
print(s2.rjust(20, "."))
