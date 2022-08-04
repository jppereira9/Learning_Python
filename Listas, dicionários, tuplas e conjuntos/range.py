# Podemos utilizar a função range para gerar listas simple:

for x in range(10) :
    print(x)

'''
- Com a mesma função range, podemos também indicar qual é o primeiro número a gerar. Para isso, 
utilizaremos dois parâmetros:

'''
print("\n")
for x in range(5, 8) :
    print(x)

'''
- Se acrescentarmos um terceiro parâmetro à função range, teremos como saltar entre os valores gerados, por exemplo, 
range(0, 10, 2) gera os pares entre 0 e 10, pois começa em 0 e adiciona 2 a cada elemento. Exemplo:

'''

print("\n")
for x in range (3, 33, 3) :
        print(x, end = " ")
print()