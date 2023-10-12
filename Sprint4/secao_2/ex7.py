def pares_ate(n: int):
    n = max(2, n)
    return (i for i in range(2, n + 1, 2))

n = 10
gerador = pares_ate(n)

for numero in gerador:
    print(numero)
