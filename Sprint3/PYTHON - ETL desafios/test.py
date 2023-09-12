# Leitura do arquivo actors.csv
with open('C:\\Users\\Ellen Cassia\\Downloads\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Removendo o cabeçalho
header = lines[0]
lines = lines[1:]

# Etapa 1: Encontrar o ator/atriz com maior número de filmes
actor_movies = {}
for line in lines:
    data = line.split(',')
    actor = data[0]
    num_movies = float(data[2])  # Converter para ponto flutuante
    actor_movies[actor] = num_movies

max_movies_actor = max(actor_movies, key=actor_movies.get)
max_movies = actor_movies[max_movies_actor]


# Escrever os resultados nos arquivos .txt correspondentes
with open('etapa-1.txt', 'w', encoding='utf-8') as file:
    file.write(f'1 - {max_movies_actor} - {max_movies} filmes\n')
