def conta_vogais(texto:str)-> int:
    texto = texto.lower()
    vogais = filter(lambda x: x in 'aeiou', texto)
    return len(list(vogais))

print(conta_vogais('Amizade'))    