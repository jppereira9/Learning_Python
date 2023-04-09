'''
Temos também como verificca se a string contém apenas caracteres em branco,
como espaços, marcas de tabulação (TAB), quebras de linha (LF) ou retorno de carro (CR).
Para isso, vamos utilizar o método isspace:

'''
x = "\t\n\r      "
print(f'{x.isspace()}')
x2 = "Alô"
print(f'{x2.isspace()}')