# Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

valores_unicos = set(speed.values()) # set() é uma função que cria um conjunto de valores únicos a partir de uma lista ou dicionário  

lista_valores_unicos = list(valores_unicos) # list() é uma função que converte um conjunto para uma lista

print(lista_valores_unicos)
