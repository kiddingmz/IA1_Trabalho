import json

# Carrega os arquivos JSON
with open('../data/coordenadas_cidades.json', 'r') as f:
    coordenadas_cidades = json.load(f)

with open('../data/rotas_cidades.json', 'r') as f:
    rotas_cidades = json.load(f)

rotas_com_coordenadas = []

for rota in rotas_cidades:
    origem = rota["origem"]
    destino = rota["destino"]

    if origem in coordenadas_cidades and destino in coordenadas_cidades:
        rota_completa = {
            "origem": {
                "cidade": origem,
                "latitude": coordenadas_cidades[origem]["latitude"],
                "longitude": coordenadas_cidades[origem]["longitude"]
            },
            "destino": {
                "cidade": destino,
                "latitude": coordenadas_cidades[destino]["latitude"],
                "longitude": coordenadas_cidades[destino]["longitude"]
            }
        }
        rotas_com_coordenadas.append(rota_completa)

with open('../data/rotas_com_coordenadas.json', 'w') as f:
    json.dump(rotas_com_coordenadas, f, indent=4)

print("Arquivo 'rotas_com_coordenadas.json' criado com sucesso!")
