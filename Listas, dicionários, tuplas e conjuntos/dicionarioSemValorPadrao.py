# Programa 6.23 - Exemplo de dicionário sem valor padrão

d = {} # Dicionário vázio
for letra in "abracadabra":
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1
print(d)