''''Para agrupar operações com lógica booleana, utilizaremos operadores lógicos, são eles:
- not (operador unário)
- and (operador binário)
- or (operador binário)
'''

'''
Operador not inverte o valor da expressão, por exemplo: 

    V | notV
    V | F
    F | v
'''
print("Operador not: \n")
print("not True =",not True) # False
print("not False =",not False) # True
print("\n")

'''
Operador and resulta em verdadeiro apenas quando seus dois operadores são verdadeiros, por exemplo:

    V1 | V2 | V1 and V2
    V  | V  |   V
    V  | F  |   F
    F  | V  |   F
    F  | F  |   F
'''
print("Operador and: \n")
print("True and True =",True and True) # True
print("True and False =",True and False) # False
print("False and True =",False and True) # False
print("False and False =",False and False) # False
print("\n")

'''
Operador or resulta em falso apenas se seus dois operadores são falsos, por exemplo:

    V1 | V2 | V1 or V2
    V  | V  |   V
    V  | F  |   V
    F  | V  |   V
    F  | F  |   F
'''
print("Operador OR: \n")
print("True or True =",True or True) # True
print("True or False =",True or False) # True
print("False or True =",False or True) # True
print("False or False =",False or False) # False


