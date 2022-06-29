# Exercicío 5.24 - Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

qnt_numeros = int(input("Digite um número: "))
if qnt_numeros < 0 :
    print("Número inválido. Digite apenas valores positivos")
else:
    if qnt_numeros >= 1:
        print("2")
        i = 1
        j = 3
        while i < qnt_numeros :
            x = 3
            while(x < j) :
                if j % x ==  0:
                    break
                x = x + 2
            if x == j :
                print(x)
                i = i + 1
            j = j + 2
