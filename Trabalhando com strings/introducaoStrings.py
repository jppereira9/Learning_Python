# Podemos acessar strings como listas, mas também strings são imutáveis em python
s = "Alô mundo" # s recebe uma string
print(s[0]) # Printa o primeiro caractere da string

# Porém não se pode alterar o valor de uma string:
# s[0] = "A" - Erro

# Para alterar o valor de uma string é preciso transforma-lá em uma lista primeiro:
# A função list transforma cada caractere da string em um elemento da lista retornada
L =  list("Alô mundo") # L recebe uma string como lista
print(L)

# A função join transforma os elementos da lista L em uma string:
s = "".join(L) 
print(s)
