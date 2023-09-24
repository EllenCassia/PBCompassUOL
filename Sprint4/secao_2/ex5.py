import csv

with open('C:\\Users\\ellen\\Intellij-Projetos\\PB-Compass-UOL\\Sprint4\\secao_2\\estudantes.csv', mode="r", newline="") as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=",")
    
    estudantes = list(map(lambda linha: {
        'nome': linha[0],
        'notas': sorted(list(map(int,linha[1:])), reverse=True)[:3],
    }, leitor_csv))

    estudantes_ordenados = sorted(estudantes, key=lambda x: x['nome'])

for estudante in estudantes_ordenados:
    print(f"Nome: {estudante['nome']} Notas: {estudante['notas']} Média: {round(sum(estudante['notas'])/len(estudante['notas']),2)} ")

