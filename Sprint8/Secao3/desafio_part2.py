import json
import boto3
import requests
from datetime import date

def lambda_handler(event, context):
    s3_bucket_name = "data-lake-de-filmes-series-raw"

    s3 = boto3.client("s3")
    
    api_key = "3470fc91a223052830e0f7162ff65bc3"
    base_url = "https://api.themoviedb.org/3"
    discover_endpoint = "/discover/movie"
    external_ids_endpoint = "/movie/{movie_id}/external_ids"

    discover_params = {
        "include_adult": False,
        "include_video": False,
        "language": "pt-BR",
        "page": 1,
        "sort_by": "vote_count.desc",
        "vote_average.gte": 8,
        "with_genres": 10749,
        "with_original_language": "en",
        "api_key": api_key
    }

    today = date.today()
    processing_date = f"{today.year}/{today.month}/{today.day}"

    movies_data = []
    arquivo_numeros = 1
    quantidade_maxima_de_arquivo = 50
    numero_maximo_de_paginas_endpoint = 111  

    for page_number in range(1, numero_maximo_de_paginas_endpoint + 1):
        discover_params["page"] = page_number

        response_discover = requests.get(base_url + discover_endpoint, params=discover_params)
        response_discover.raise_for_status() 
        data_discover = response_discover.json()

        for movie in data_discover.get("results", []):
            movie_id = movie.get("id")

            response_external_ids = requests.get(base_url + external_ids_endpoint.format(movie_id=movie_id), params={"api_key": api_key})
            response_external_ids.raise_for_status()  
            data_external_ids = response_external_ids.json()

            imdb_id = data_external_ids.get("imdb_id")

            movie["imdb_id"] = imdb_id

            movies_data.append(movie)

        # Verifica se atingiu a quantidade máxima ou a última página
        if len(movies_data) >= quantidade_maxima_de_arquivo or page_number == numero_maximo_de_paginas_endpoint:
            send_to_s3(movies_data, s3, s3_bucket_name, processing_date, arquivo_numeros)
            movies_data = []
            arquivo_numeros += 1

    return {
        'statusCode': 200,
        'body': json.dumps('Dados enviados para o S3 com sucesso!')
    }

def send_to_s3(data, s3, bucket_name, processing_date, index):
    serialized_data = json.dumps({"results": data}, ensure_ascii=False, indent=4)
    filename = f"dados_filmes_page_{index}.json"
    s3_object_key = f"Raw/TMDB_API/JSON/{processing_date}/{filename}"
    s3.put_object(Body=serialized_data, Bucket=bucket_name, Key=s3_object_key)
