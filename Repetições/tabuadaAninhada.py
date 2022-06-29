# Imprime as tabuadas de 1 a 10

tabuada = 1 # Contador
while tabuada <= 10 :
    numero = 1 # Contador
    while numero <= 10 :
        print("{} x {} = {:1.0f}" . format(tabuada, numero, tabuada * numero))
        numero += 1 # Incrementa numero
    print("\n")
    tabuada += 1 # Incrementa tabuada