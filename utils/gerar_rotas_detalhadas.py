import json
import requests
import random
import time
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv('API_KEY')

headers = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json'
}

with open('../data/rotas_com_coordenadas.json', 'r') as f:
    rotas_com_coordenadas = json.load(f)

condicoes_estrada = ["Boa", "Moderada", "Ruim"]

rotas_detalhadas = []


def obter_detalhes_rota(origem_coords, destino_coords):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    # Dados para a requisição
    payload = {
        "coordinates": [origem_coords, destino_coords],
        "profile": "driving-car",
        "format": "json",
        "radiuses": [5000]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 429:
            print("Limite de requisições por minuto atingido (HTTP 429). Aguardando para tentar novamente...")
            time.sleep(60)
            return obter_detalhes_rota(origem_coords, destino_coords)

        if response.status_code == 403:
            print("Limite diário de requisições atingido (HTTP 403). Encerrando.")
            return None, None, "Limite Diário Excedido"

        response.raise_for_status()

        rota = response.json()

        if 'routes' not in rota:
            print(f"Erro: 'routes' não encontrado na resposta. Resposta da API: {rota}")
            return None, None, None

        distancia = rota['routes'][0]['summary']['distance']
        duracao = rota['routes'][0]['summary']['duration']

        condicao_estrada = random.choice(condicoes_estrada)

        return distancia, duracao, condicao_estrada

    except requests.exceptions.HTTPError as errh:
        print(f"Erro HTTP: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Erro na requisição: {err}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return None, None, None


for rota in rotas_com_coordenadas:
    origem = rota["origem"]
    destino = rota["destino"]

    origem_coords = [origem["longitude"], origem["latitude"]]
    destino_coords = [destino["longitude"], destino["latitude"]]

    distancia, duracao, condicao_estrada = obter_detalhes_rota(origem_coords, destino_coords)

    if distancia is not None:
        rota_detalhada = {
            "origem": origem["cidade"],
            "destino": destino["cidade"],
            "distancia_metros": distancia,
            "duracao_segundos": duracao,
            "condicao_estrada": condicao_estrada,
            "coordenadas": {
                "origem": origem_coords,
                "destino": destino_coords
            }
        }
        rotas_detalhadas.append(rota_detalhada)

with open('../data/rotas_detalhadas.json', 'w') as f:
    json.dump(rotas_detalhadas, f, indent=4)

print("Arquivo 'rotas_detalhadas.json' criado com sucesso!")
