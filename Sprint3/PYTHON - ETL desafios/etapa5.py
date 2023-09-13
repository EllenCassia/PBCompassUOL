# Leitura do arquivo actors.csv
with open('C:\\Users\\ellen\\Downloads\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Removendo o cabeçalho
header = lines[0]
lines = lines[1:]

actor_total_gross = {}

for line in lines:
    data = line.split(',')
    try:
        gross = float(data[1])  # Converte a coluna "Gross" para ponto flutuante
        actor = data[0]
        actor_total_gross[actor] = gross
    except ValueError:
        continue

with open('etapa-5.txt', 'w', encoding='utf-8') as file:
   for actor, total_gross in actor_total_gross.items():
        file.write(f"{actor} - {total_gross:.2f}\n")