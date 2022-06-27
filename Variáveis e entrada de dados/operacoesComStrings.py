# As variáveis de tipo string suportam operações como fatiamento, concatenação e composição


# Concatenação: O conteúdo de variáveis string podem ser somados, ou melhor, concatenados.


s = "ABC"
print(s + "C") # ABBC

print(s + "D" * 4) # ABCDDDD
print("X" + "-" * 10 + "X") # x----------x

print(s + "x4 = " + s * 4) # ABCx4ABCABCABCABC

# Concatenação só pode ser usado com strings!
'''
nome = "Tião"
idade = 10
print(nome + idade) - Erro

'''
'''
- Composição:  Juntar várias strings para construir uma mensagem nem sempre é prático. Por exemplo:
exibir que "João Tem X anos", em que X é uma variável númerica.

- Usando a composição de strings do Python, podemos escrever de forma simples e clara: "João tem %d ano" %X

'''

x = 21
print("Joao tem %d anos" % x)

# Marcadores: %d - Números inteiros, %s - Strings e %f - Números decimais

idade = 22
print("[%d]" % idade) # [22]
print("[%03d]" % idade) # [022]
print("[%3d]" % idade) # [ 22]
print("[%-3d]" % idade) # [22 ]

# Quando formatamos números decimais, podemos utilizar dois valores entre o símbolo de % e a letra f. Exemplos:

print("%5f" % 5) # 5.00000
print("%5.2f" % 5) # 5.00
print("%10f" % 5) # 5.0000000000

'''
- O poder da composição realmente aparece quando precisamos combinar vários valores em uma nova string. Exemplo

'''
print("%s tem %d anos, tem R$%.2f no bolso e estuda %s" % ("Joao", 21, 34.50, "Ciencia da Computacao"))


'''
- Fatiamento: O fatiamento funciona com a utilização de dois pontos no índice da string. Exemplos:

'''

s = "ABCDEFGHI"
print(s[0:2]) # ABC
print(s[1:2]) # B
print(s[2:4]) # CD
print(s[1:8]) # BCDEFGH

'''
- Podemos também utilizar valores negativos para indicar posições a partir da direita. Assim -1
é o último caractere; -2 o penúltimo; e assim por diante. Veja o resultado dos testes com índices negativos.

'''
s = "ABCDEFGHI"
print(s[:2]) # AB
print(s[1: ]) # BCDEFGHI
print(s[0:-2]) # ABCDEFGH
print(s[:]) # ABCDEFGHI
print(s[-1:]) # I
print(s[-5: 7]) # EFG
print(s[-2:-1]) # H
