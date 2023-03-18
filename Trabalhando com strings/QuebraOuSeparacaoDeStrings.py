'''

O método split quebra uma string a partir de um caractere passado como parâmetro,
retornando uma lista coms as substrings já separadas:

'''
string1 = "Palmeiras, Verdão, SEP, Maio Campeão do Brasil"
print(string1.split(","))

# Se você deseja separa uma sting, com várias linhas de texto, pode utilizar o método splitlines:
string2 = "Uma linha\noutra linha\ne mais uma\n"
print(f"{string2}")
print(string2.split())