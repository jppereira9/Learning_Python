'''
- Observe que um gerador como o retorno pela função range não é exatamente uma lista. Embora seja usado de forma
parecida, é, na realidade, um objeto de outro tipo. Para transformar um gerador em lista, utilize a função lista:

'''

# Programa 6.10 - Transformação de range em uma lista
L = list(range(100, 1100, 50))
print(L)