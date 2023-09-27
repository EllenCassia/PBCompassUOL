def maiores_que_media(conteudo:dict)->list:
    produtos = list(filter(lambda x: x[1] > sum(conteudo.values()) / len(conteudo.values()), conteudo.items()))
    return sorted(produtos, key=lambda x: x[1])
    
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99,
}

print(maiores_que_media(conteudo))
