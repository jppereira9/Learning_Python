'''
Strings em Python podem ter seu conteúdo analisado e verificado tulizando-se métodos especiais.
Esses métodos verificam se todos os caracteres são letras, números ou uma combinação deles.

Vejamos alguns exemplos:

'''
s  = "125"
p = "Olá Mundo"
# O método isnum retorna verdadeiro se a strings não estiver vazia ou seus caracteres são letra e/ou números
print(f'{s.isalnum()}')
print(f'{p.isalnum()}')