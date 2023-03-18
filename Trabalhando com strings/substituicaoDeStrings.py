'''
Para substituir trechos de uma string por outros, utilize o método replace.
Com o método replace, o primeiro parâmetro é a string a substituir; e o segundo,
o conteúdo que a substituirá

'''
string1 = "Um tigre, dois tigres, três tigres"
print(string1.replace("tigre", "gato"))

print(string1.replace("tigre", "gato", 1)) # Opcionalmente podemos utilizar um 3º parâmetro que limita quantas vezes queemos realizar a repetição.

print(string1.replace("tigre", "gato", 2))

print(string1.replace("tigre", ""))
'''
Se você passar uma string vazia no segundo parâmetro, o trecho será apagado. Se o primeiro parâmetro
for uma string vazia, o segundo será inserido antes de cada caractere da string.
'''
print(string1.replace("", "-"))