# O método strip é utilizado para remover espaços em branco do início ou fim da string.

string1 = "          Olá          "
print(f'{string1}')
print(string1.strip())

'''
Já os métodos lstrip e rstring removem apenas os caracteres em branco à direita ou à
esquerda, respectivamente

'''
print(f'{string1}')
print(f'{string1.lstrip()}')
print(f'{string1.rstrip()}')

''''
Se você passar um parâmetro tanto para strip quanto para lstip ou rstip, este seá utilizado
como caractere a remover

'''

string2 = "...///Olá///..."
print(f'{string2.lstrip(".")}')

print(f'{string2}')
print(f'{string2.rstrip(".")}')

print(f'{string2}')
print(f'{string2.strip(".")}')
