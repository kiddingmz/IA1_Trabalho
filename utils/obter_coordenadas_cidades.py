from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()
ORS_API_KEY = os.getenv('API_KEY')

def obter_coordenadas_ors(cidade, pais="Moçambique"):
    url = "https://api.openrouteservice.org/geocode/search"
    params = {
        "api_key": ORS_API_KEY,
        "text": f"{cidade}, {pais}",
        "boundary.country": "MZ",
        "size": 1
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["features"]:
            coords = data["features"][0]["geometry"]["coordinates"]
            return (coords[1], coords[0])
    return None


cidades = [
    "Angoche", "Beira", "Catandica", "Chibuto", "Chimoio", "Chokwé",
    "Cuamba", "Dondo", "Garue", "Gondola", "Gurué", "Inhambane",
    "Lichinga", "Macia", "Manica", "Manjacaze", "Maputo", "Matola",
    "Maxixe", "Moatize", "Ilha de Moçambique", "Mocimboa",
    "Mocuba", "Monapo", "Montepuez", "Mutuáli", "Nacala", "Namialo",
    "Nampula", "Pemba", "Quelimane", "Tete", "Ulongué", "Vilanculos", "Xai-Xai"
]

dados_cidades = {}

for cidade in cidades:
    coords = obter_coordenadas_ors(cidade)
    if coords:
        dados_cidades[cidade] = {"latitude": coords[0], "longitude": coords[1]}
        print(f"Coordenadas de {cidade}: Latitude = {coords[0]}, Longitude = {coords[1]}")
    else:
        dados_cidades[cidade] = {"latitude": None, "longitude": None}
        print(f"Coordenadas para {cidade} não foram encontradas.")


with open("../data/coordenadas_cidades.json", "w") as json_file:
    json.dump(dados_cidades, json_file, indent=4, ensure_ascii=False)

print(f"Dados salvos em coordenadas_cidades.json")