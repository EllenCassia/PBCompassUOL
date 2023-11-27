import random
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand,lit
from pyspark.sql.functions import year
from pyspark.sql.types import StringType

spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("C:\\Users\\ellen\\Intellij-Projetos\\PB-Compass-UOL\\Sprint8\\Secao4\\Tarefa4\\nomes_aleatorios.txt", header=True)

# 1 etapa
# df_nomes.show(5)

# # 2 etapa
df_nomes = df_nomes.withColumnRenamed("nomes_aleatorios", "Nomes")

# df_nomes.printSchema()

# df_nomes.show(10)

# # 3 etapa
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 0.33, "Fundamental")
                                           .when((rand() >= 0.33) & (rand() < 0.67), "Médio")
                                           .otherwise("Superior"))

# df_nomes.show(10)

paises_americadosul = ["Brasil", "Argentina", "Chile", "Colômbia", "Equador", "Uruguai", "Paraguai", "Peru", "Venezuela", "Bolívia", "Guiana", "Suriname", "Guiana Francesa"]

# Adicione uma coluna "Random" com números inteiros aleatórios
df_nomes = df_nomes.withColumn("Random", lit(random.randint(0, len(paises_americadosul))))

# Adicione uma coluna "País" com seleção aleatória baseada na coluna "Random"
# df_nomes = df_nomes.withColumn("País", paises_americadosul[(col("Random") * len(paises_americadosul)).cast("int")])

# # Exiba o DataFrame resultante
# df_nomes.show(10)

df_nomes_com_ano = df_nomes.withColumn("AnoNascimento", (lit(1945) + (rand() * (2010 - 1945))).cast("int"))

# Pergunta 6
df_select = df_nomes.select("*").filter(year("AnoNascimento") >= 2000).limit(10)

df_select.show(5)

# # Pergunta 7
# df_nomes.createOrReplaceTempView("pessoas")
# result_7 = spark.sql("SELECT COUNT(*) FROM pessoas WHERE YEAR(data_nascimento) BETWEEN 1980 AND 1994").show()

# # Pergunta 8
# result_8 = spark.sql("SELECT COUNT(*), Pais, Geração FROM pessoas WHERE YEAR(data_nascimento) BETWEEN 1980 AND 1994 GROUP BY Pais, Geração ORDER BY Pais, Geração").show()