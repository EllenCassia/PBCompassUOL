# Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores.
# Estamos falando aqui da média da coluna Gross.

# Leitura do arquivo actors.csv
with open('C:\\Users\\ellen\\Downloads\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Removendo o cabeçalho
header = lines[0]
lines = lines[1:]

total_gross = 0  # Inicializa a variável para armazenar a soma das receitas brutas
count = 0  # Inicializa a variável para contar o número de filmes

for line in lines:
    data = line.split(',')
    try:
        gross = float(data[5])  # Converte a coluna "Gross" para ponto flutuante
        total_gross += gross
        count += 1
    except ValueError:
        continue  # Ignora linhas com valores não válidos


with open('etapa-2.txt', 'w', encoding='utf-8') as file:
    if count > 0:
        average_gross = total_gross / count
        file.write(f"A média de receita de bilheteria bruta dos principais filmes é de ${average_gross:.2f} milhões.")

