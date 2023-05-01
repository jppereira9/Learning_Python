'''
Quando usamos funções, começamos a trabalhar com variáveis internas ou locais e com variáveis
externas ou globais. A diferença entre elas é a visibilidade ou escopo.

'''

# Vejamos um exemplo dos dois casos:
EMPRESA = "Unidos Benceremos Ltda" # Variável global
def imprime_cabecalho(): # Definindo a função
    print(f'{EMPRESA}')
    print(f'-' * len(EMPRESA))

imprime_cabecalho()

'''
A função imprime_cabecalho não reebe parâmetros e nem retorna valores. Ela simplesmente imprime
o nome da empresa e traços. Observe que utilizamos a variável EMPRESA definida fora da função, nesse
caso EMPRESA é uma variável global, podendo ser acessado em qualquer função.

--> Variáveis globais devem ser utilizadas o mínimo possível em programas, pois dificultam sua leitura
em violam o encapsulamento da função.

'''

'''
Devido à capacidade da linguagem Python de declarar variáveis à medida que precisarmos, devemos
tomar cuidado quando alteramos uma variável global dentro de uma função. Vejamos um exemplo:

'''
a = 5 # Variável global
def muda_e_imprime(): # Definição da função
    a = 7
    print(f'A dentro da função: {a}')
print(f'A antes de mudar: {a}')
muda_e_imprime() # Invocando a função
print(f'A depois de mudar: {a}')
print("\n")
'''
Se quisermos modificar uma variável global dentro de uma função, devemos informar que estamos
usando uma variável global antes de iniializá-la, na primeira linha de nossa função. Essa função
é feita om a instrução global. Vejamos um exemplo modificado;

'''
print("\n")
b = 5 # Variável global
def muda_e_imprime2(): #Definindo a função
    global b
    b = 7
    print(f'B dentro da função:{b}')
print(f'B antes de mudar: {b}')
muda_e_imprime2()
print(f'B depois de mudar {b}')