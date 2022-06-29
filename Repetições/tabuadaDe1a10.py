# Vejamos outro exemplo da impressão da tabuada de 1 a 10, mas sem utlizar repetições aninhadas:

tabuada = 1
numero = 1
while tabuada <= 10 :
    print("{} x {} = {:1.0f}" .format(numero, tabuada, tabuada * numero))
    numero += 1
    if numero == 11 :
        numero = 1
        tabuada += 1
        print("\n")