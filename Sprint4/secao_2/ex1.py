from functools import reduce

with open('number.txt', 'r') as arquivo:
    number = list(map(lambda x: int(x), arquivo.readlines()))

pares = filter(lambda x: int(x) % 2 == 0, number)
cincoMaiores = sorted(pares, reverse=True)[:5]
soma = sum(cincoMaiores)

print(cincoMaiores)
print(soma)
