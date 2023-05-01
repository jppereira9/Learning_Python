'''
Exercício 8.11 - Escreva uma função para validar uma variável string. Essa função reebe como parâmetro a string,
o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre
os valores de máximo e minimo, e falso, caso contrário

'''

def validaString(string, min, max): # Definindo a função
    if len(string) >= min and len(string) <= max: # O tamanho da string precisar estar entre min e max
        return True
    else:
        return False

print(validaString("Banana", 1, 10)) # True - string tem mais que 1 e menos que 10
print(validaString("Fé", 5, 10)) # False - string tem menos que 5 caracteres
print(validaString("Analfabeto", 1, 8)) # False - string tem mais que 8 caracteres
