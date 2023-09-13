a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Converte as listas em conjuntos (sets)
set_a = set(a)
set_b = set(b)

# Encontra a interseção entre os conjuntos
intersecao = set_a.intersection(set_b)

# Converte a interseção de volta em uma lista (opcional)
lista_intersecao = list(intersecao)

# Imprime a lista de valores da interseção
print(lista_intersecao)
