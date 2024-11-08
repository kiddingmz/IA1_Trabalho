import json
import os
from collections import deque


def busca_largura(grafo, cidade_origem, cidade_destino, penalizacao_ruim=1.5):
    fila = deque([(cidade_origem, [], 0)])
    cidades_visitadas = set()

    while fila:
        cidade_atual, caminho_atual, distancia_total = fila.popleft()

        if cidade_atual == cidade_destino:
            return caminho_atual + [cidade_atual], distancia_total

        if cidade_atual in cidades_visitadas:
            continue

        cidades_visitadas.add(cidade_atual)

        for vizinho, dados in grafo[cidade_atual].items():
            if vizinho not in cidades_visitadas:
                penalizacao = penalizacao_ruim if dados['condicao_estrada'] == "Ruim" else 1
                fila.append(
                    (vizinho, caminho_atual + [cidade_atual], distancia_total + dados['distancia'] * penalizacao))

    return None


def carregar_dados():
    with open(os.path.join(os.path.dirname(__file__), '../data/heuristica.json'), 'r') as file:
        heuristica = json.load(file)

    cidade_origem = heuristica["origem"]["cidade"]
    cidade_destino = heuristica["destino"]["cidade"]

    with open(os.path.join(os.path.dirname(__file__), '../data/rotas_detalhadas.json'), 'r') as file:
        rotas_detalhadas = json.load(file)

    grafo = {}
    for rota in rotas_detalhadas:
        origem = rota["origem"]
        destino = rota["destino"]
        distancia_metros = rota["distancia_metros"]
        condicao_estrada = rota["condicao_estrada"]

        if origem not in grafo:
            grafo[origem] = {}
        if destino not in grafo:
            grafo[destino] = {}

        grafo[origem][destino] = {
            "distancia": distancia_metros / 1000,
            "condicao_estrada": condicao_estrada
        }
        grafo[destino][origem] = {
            "distancia": distancia_metros / 1000,
            "condicao_estrada": condicao_estrada
        }

    return grafo, cidade_origem, cidade_destino


def main():
    grafo, cidade_origem, cidade_destino = carregar_dados()
    melhor_rota = busca_largura(grafo, cidade_origem, cidade_destino, penalizacao_ruim=1.5)

    if melhor_rota:
        caminho, distancia = melhor_rota
        print(
            f"A melhor rota de {cidade_origem} para {cidade_destino} é: {' -> '.join(caminho)} com distância total de {distancia:.2f} km")
    else:
        print(f"Não foi possível encontrar uma rota entre {cidade_origem} e {cidade_destino}.")


if __name__ == "__main__":
    main()
