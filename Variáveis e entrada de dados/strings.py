'''
- Variáveis do tipo string armazenam cadeias de caracteres como nomes e texto em geral.

- Para possibilitar a seperação entre o texto do seu programa e o contéudo de uma string, utilizaremos aspas(") para 
delimitar o inicío e o fim da sequência de caracteres.

- O tamanho de uma string pode ser obtiddo utilizando-se a função len. A função len retorna um valor do tipo inteiro,
representando a quantidade de caracteres contidos na string
'''
print(len("A")) # 1
print(len("AB")) # 2
print(len("")) # 0 - String vazia
print(len("O rato roeu a roupa")) # 19

'''
-  Como dito anteriormentr, outra característica de strings é poder acessar seu conteúdo caractere a caractere.

- Para acessar os caracteres de uma string, devemos informar o índice ou posição do caractere entre colchetes ([]) 
'''
a = "ABCDEF" # String com 6 índices [0,1,2,3,4,5]
print(a[0]) # A
print(a[1]) # B
print(a[5]) # F
# print(a[6]) - Acessando um índice inválido da string
