import random
import names
import pandas as pd

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

nomes_unicos = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

dados = [random.choice(nomes_unicos) for _ in range(qtd_nomes_aleatorios)]

df = pd.DataFrame(dados, columns=['nomes_aleatorios'])

df.to_csv('nomes_aleatorios.txt', index=False)

