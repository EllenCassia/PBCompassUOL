import os
from datetime import date
import boto3

# Cria sessão com credenciais e região padrão
aws_session = boto3.Session(
    aws_access_key_id="AKIAXFDXCMA2CQU4UTX6",  # IAM principal
    aws_secret_access_key="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",  # IAM principal
    region_name="us-east-1",
)

# Cria cliente para S3
s3 = aws_session.client("s3")

# Configura as informações padrão
today = date.today()
bucket_name = "data-lake-de-filmes-series-raw"
storage_layer = "Raw"
data_origin = "Local"
# O formato dos dados está hard coded por conta do exercício, mas ele pode ser dinâmico,
# como a especificação dos dados, gerada mais abaixo.
data_format = "CSV"
processing_date = f"{today.year}/{today.month}/{today.day}"

# Listo todos os arquivos no diretório do script e procedo ao processamento do arquivo caso seja de extensão CSV
for file in os.listdir():
    if file.endswith(".csv"):
        # Gero a especificação do dado a partir do nome do arquivo
        data_specification = file.split(".")[0].title()
        # Gero o caminho absoluto ao arquivo.
        file_path = os.path.abspath(file)
        # Com os dados anteriores eu termino de completar o caminho no bucket.
        bucket_path = f"{storage_layer}/{data_origin}/{data_format}/{data_specification}/{processing_date}/{file}"
        # Realizo o upload dos arquivos para a S3.
        s3.upload_file(file_path, bucket_name, bucket_path)
