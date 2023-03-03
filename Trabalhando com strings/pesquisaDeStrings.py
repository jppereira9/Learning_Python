# Para pesquisar se uma string está dentro de outra e obter a posição da primeira ocorrência, use find
s = "Olá mundo"
print(f'{s.find("mun")}')

# Caso a string seja encontrada, você obterá um valor maior ou igual a zero, ou -1 caso contrário
print(f'{s.find("ok")}')

t = "Um dia de sol"
print(f'{t.rfind("d")}') # 7

print(f'{t.find("d")}') # 3

'''
Tanto find quanto rfind suportam duas opções adicionais: inicio(start) e fim(end). Se você especificar o ínicio, 
a pesquisa começará a partir dessa posição. Se especificar o fim, a pesquisa utilizará essa posição como último 
caractere a considerar na pesquisa. Exemplo
'''
r = "um tigre, dois tigres, três tigres"
print(f'{r.find("tigres")}')
print(f'{r.rfind("tigres")}')
print(f'{r.find("tigres", 7)}') # Inicio = 7
print(f'{r.find("tigres", 30)}') # Inicio = 30
print(f'{r.find("tigres", 0, 10)}') # Inicio = 0  e fim = 10
