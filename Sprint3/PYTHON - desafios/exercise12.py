import json

# Abra o arquivo JSON em modo de leitura
with open('person.json', 'r') as arquivo:
    # Faça o parsing do conteúdo do arquivo
    dados = json.load(arquivo) # converter os dados em uma estrutura de dados Python

# Imprima o conteúdo do JSON
print(dados)
