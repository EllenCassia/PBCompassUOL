# Leitura do arquivo actors.csv
with open('C:\\Users\\Ellen Cassia\\Downloads\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Removendo o cabeçalho
header = lines[0]
lines = lines[1:]

actor_movies = []

for line in lines:
    data = line.split(',')
    number_of_movies = float(data[2])  
    actor = data[0]  
    actor_movies.append((actor, number_of_movies))  
 
if actor_movies:
    max_number_of_movies = -1  
    actor_with_max_movies = None

    for actor, number_of_movies in actor_movies:
        if number_of_movies > max_number_of_movies:
            max_number_of_movies = number_of_movies
            actor_with_max_movies = actor


# Escrever os resultados nos arquivos .txt correspondentes
with open('etapa-1.txt', 'w', encoding='utf-8') as file:
    file.write(f'1 - {actor_with_max_movies} - {max_number_of_movies:.2f} filmes')
