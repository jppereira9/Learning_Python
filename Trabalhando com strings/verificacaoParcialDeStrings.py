'''
Quando é necessário verificar se uma string começa ou termina com alguns caracteres, pode ser usaso os métodos 
startswith e endswith:
'''
# Esses métodos verificam apenas os primeiros ou os últimos caracteres da string e retorna True ou False:

# startswith:
nome = "João Pedro" # Nome recebe "João Pedro"
print(nome.startswith("João")) # nome começa com João - True
print(nome.startswith("joão")) # nome começa com joão - False

# endswith:
print(nome.endswith("Pedro")) # nome termina com Pedro - True
print(nome.endswith("pedro")) # nome termina com pedro - False

'''
O método lower retorna uma cópia da string com todos os caracteres minúsculos, e o método upper retorna uma cópia
com todos os caracteres maiúsculos.
'''
s = "O rato roeu a roupa do Rei de Roma"
print(s)
print(s.lower()) # Transforma todos os caracteres em minúsculos
print(s.upper()) # Transforma todos os caracteres em maiúsculo

print(nome.lower().startswith("joão")) # Transforma todos os caracteres em minúsculos e verifica se começa com joão
print(nome.upper().startswith("JOÃO")) # Transoforma todos os caracteres em maiúsculos e verifica se começa com joão

# Outra forma de verificar se uma palavra pertence a uma string é utilizando o operador in:

a = "Maria Amélia da Silva" # a recebe a string Maria Amélia da Silva
print("Amélia" in a) # Amélia está na string a ? - True
print("Maria" in a) # Maria está na string a ? - True
print("Silva" in a) # Silva está na string a ? - True
print("A" in a) # A está na string a ? - True
print("amélia" in a) # amélia está na string a ? - False

# Você também pode testar se uma string não está contida em outra, tulizando o not in:
c = "Todos os caminhos levam a Roma"
print("levam" not in c) # levam não está em c ? - False
print("Caminhos" not in c) # Caminhos não está em c ? - True
print("AS" not in c) # AS não está em c ? - True

'''
Veja que aqui também letras maiúsculas e minúsculas são diferentes. Você pode combinar lower e upper 
com in e not in para ignorar esse tipo de diferença:
'''

f = "João comprou um carro" # f recebe uma string
print("joão" in f.lower()) # True
print("CARRO" in f.upper()) # True
print("comprou" not in f.lower()) #False
print("barco" not in f.upper()) # True
