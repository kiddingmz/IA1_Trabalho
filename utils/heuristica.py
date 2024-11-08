import json
import math
import os


def calcular_distancia_haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c
    return distancia


def main():
    dados_distancias = {}
    with open(os.path.join(os.path.dirname(__file__), "../data/coordenadas_cidades.json"), "r") as file:
        coordenadas_cidades = json.load(file)

    cidade_origem = input("Informe a cidade de origem: ")
    cidade_destino = input("Informe a cidade de destino: ")

    coords_origem = coordenadas_cidades.get(cidade_origem)
    coords_destino = coordenadas_cidades.get(cidade_destino)

    if not coords_origem:
        print(f"Coordenadas para a cidade de origem '{cidade_origem}' não foram encontradas.")
    elif not coords_destino:
        print(f"Coordenadas para a cidade de destino '{cidade_destino}' não foram encontradas.")
    else:
        dados_distancias = {
            "origem": {
                "cidade": cidade_origem,
                "latitude": coords_origem["latitude"],
                "longitude": coords_origem["longitude"]
            },
            "destino": {
                "cidade": cidade_destino,
                "latitude": coords_destino["latitude"],
                "longitude": coords_destino["longitude"]
            },
            "distancias": {}
        }

    for cidade, coordenadas in coordenadas_cidades.items():
        if coordenadas["latitude"] is not None and coordenadas["longitude"] is not None:
            coords_cidade = (coordenadas["latitude"], coordenadas["longitude"])
            coords_destino_tuple = (coords_destino["latitude"], coords_destino["longitude"])

            distancia = calcular_distancia_haversine(
                coords_cidade[0], coords_cidade[1],
                coords_destino_tuple[0], coords_destino_tuple[1]
            )
            dados_distancias["distancias"][cidade] = {
                "latitude": coordenadas["latitude"],
                "longitude": coordenadas["longitude"],
                "distancia_ate_destino_km": distancia
            }
            print(f"Distância de {cidade} até {cidade_destino}: {distancia:.2f} km")
        else:
            dados_distancias["distancias"][cidade] = {
                "latitude": None,
                "longitude": None,
                "distancia_ate_destino_km": None
            }
            print(f"Coordenadas para {cidade} não foram encontradas.")

    with open(os.path.join(os.path.dirname(__file__), '../data/heuristica.json'), "w") as json_file:
        json.dump(dados_distancias, json_file, indent=4, ensure_ascii=False)

    print(f"Dados salvos em heuristica.json")


if __name__ == "__main__":
    main()
