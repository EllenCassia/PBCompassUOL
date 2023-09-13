# Leitura do arquivo actors.csv
with open('C:\\Users\\ellen\\Downloads\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Removendo o cabeçalho
header = lines[0]
lines = lines[1:]

actor_movies = []

# Inicializa variáveis para rastrear o ator com o maior número de filmes
max_number_of_movies = 0
actor_with_max_movies = ""

for line in lines:
    data = line.split(',')
    try:
        number_of_movies = int(data[2])  # Converte para inteiro
        actor = data[0]  # Nome do ator
        actor_movies.append(actor)  # Adiciona o nome do ator à lista
        if number_of_movies > max_number_of_movies:
            max_number_of_movies = number_of_movies
            actor_with_max_movies = actor
    except ValueError: # Ignora linhas com valores não válidos
        continue 

with open('etapa-1.txt', 'w', encoding='utf-8') as file:
    file.write(f'1 - {actor_with_max_movies} - {max_number_of_movies:.2f} filmes')