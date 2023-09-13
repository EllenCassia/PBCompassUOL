# Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. 
# Considere a coluna Avarage per Movie para fins de cálculo.

# Leitura do arquivo actors.csv
with open('C:\\Users\\ellen\\Downloads\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Removendo o cabeçalho
header = lines[0]
lines = lines[1:]

max_average_gross = 0  # Inicializa a variável para rastrear a maior média
actor_with_max_average = ""  # Inicializa a variável para rastrear o ator com a maior média

for line in lines:
    data = line.split(',')
    actor = data[0]
    try:
        average_per_movie = float(data[3])  # Converte a coluna "Average per Movie" para ponto flutuante
        if average_per_movie > max_average_gross:
            max_average_gross = average_per_movie
            actor_with_max_average = actor
    except ValueError:
        continue  # Ignora linhas com valores não válidos

with open('etapa-3.txt', 'w', encoding='utf-8') as file:
    if actor_with_max_average:
        file.write(f"O ator/atriz com a maior média de receita de bilheteria bruta por filme é {actor_with_max_average} com uma média de ${max_average_gross:.2f} milhões por filme.")  