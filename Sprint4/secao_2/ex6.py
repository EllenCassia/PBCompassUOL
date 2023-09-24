
def menores_que_media(conteudo:dict)->list:
    return sorted(list(filter(lambda x: x[1] > sum(conteudo.values())/len(conteudo), conteudo.items())), reverse=True)


print(menores_que_media({
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}))       

