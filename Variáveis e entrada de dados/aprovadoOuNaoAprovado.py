'''
 - Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado,
todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
está armazenada nas seguintes variáveis: materia1, materia2 e materia3.
'''

materia1 = 7 # materia1 recebe 7
materia2 = 8 # materia2 recebe 8
materia3 = 9 # materia3 recebe 9

# Aprovado = False
aprovado = materia1 > 7  and materia2 > 7 and materia3 > 7
print("Aprovado = ", aprovado)

materia1 = 8 # materia1 recebe 8
materia2 = 10 # materia2 recebe 10
materia3 = 8 # materia3 recebe 8

# Aprovado = True
aprovado = materia1 > 7  and materia2 > 7 and materia3 > 7
print("Aprovado = ", aprovado)

materia1 = 9 # materia1 recebe 9
materia2 = 10 # materia2 recebe 10
materia3 = 10 # materia3 recebe 10

# Aprovado = True
aprovado = materia1 > 7  and materia2 > 7 and materia3 > 7
print("Aprovado = ", aprovado)

