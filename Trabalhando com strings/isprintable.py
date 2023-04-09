'''
Se você precisar verifica se algo pode ser impresso na tela, o método isprintable
pode ajudar. Ele retorna False se algum caractere que não pode ser impresso for 
encontrado na string. Você pode utilizá-lo para veificar se a impressão de uma 
string pode causar efeitos indesejados no terminal ou na formatação de um arquivo

'''
a = "\n\t"
b = "\nAlô"
c = "Alô Mundo"
print(f'{a.isprintable()}')
print(f'{b.isprintable()}')
print(f'{c.isprintable()}')
