# Utilizando a função random
import random
for x in range(10):
    print(random.random())

# Utilizando a função uniform:
for x in range(10):
    print(random.uniform(15, 25))

# Utilizando a função sample:
print(random.sample(range(1, 101), 6))

a = list(range(1, 11))
random.shuffle(a)
print(a)
