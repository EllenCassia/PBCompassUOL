# Leitura do arquivo actors.csv
with open('C:\\Users\\ellen\\Downloads\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Removendo o cabeçalho
header = lines[0]
lines = lines[1:]

contagem_filmes = {}

for line in lines:
    data = line.split(',')
    try:
        if len(data) >= 5:  # Verifica se há pelo menos 5 elementos (incluindo o filme)
            movie = data[4].strip()  # Remove espaços em branco em excesso no nome do filme
            if movie in contagem_filmes:
                contagem_filmes[movie] += 1
            else:
                contagem_filmes[movie] = 1
    except ValueError:
        continue  # Ignora linhas com valores não válidos    

filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: x[1], reverse=True)

with open('etapa-4.txt', 'w', encoding='utf-8') as file:
    for filme, contagem in filmes_ordenados:
        file.write(f"{filme} apareceu {contagem} vezes na lista de filmes.\n")