# Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# Use um conjunto (set) para armazenar valores únicos
valores_unicos = set(speed.values())

# Em seguida, converta o conjunto de volta para uma lista
lista_valores_unicos = list(valores_unicos)

print(lista_valores_unicos)
