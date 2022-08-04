'''
- Com a função enumerate podemos ampliar as funcionalidades de for facilmente. Vejamos como imprimir uma lista, em que
teremos o índice entre colchetes e o valor à sua direita:

'''
L = [5, 9, 13]
x = 0
for e in L :
    print("[{}] {}" .format(x, e))
    x += 1

# Vejamos agora o mesmo programa, mas utilizando a função enumerate:
print("\nUtilizando o Enumerate:\n")
L = [5, 9, 13]
for x, e in enumerate(L) :
    print("[{}] {}" .format(x, e))
   