# Programa 6.24 - Exemplo de dicionario com valor padrão

d = {} # Dicionário vazio
for letra in "abracadabra":
    d[letra] = d.get(letra, 0) + 1
print(d)