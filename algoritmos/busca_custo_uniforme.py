import heapq
import json
import os


def busca_custo_uniforme(grafo, cidade_origem, cidade_destino):
    fila_prioridade = [(0, cidade_origem, [])]
    visitados = set()
    melhor_rota = None

    while fila_prioridade:
        custo_acumulado, cidade_atual, caminho_atual = heapq.heappop(fila_prioridade)

        if cidade_atual in visitados:
            continue
        visitados.add(cidade_atual)

        caminho_atual.append(cidade_atual)

        if cidade_atual == cidade_destino:
            melhor_rota = (caminho_atual, custo_acumulado)
            break

        for vizinho, dados in grafo[cidade_atual].items():
            if vizinho not in visitados:
                custo = dados['tempo_viagem']
                if dados['condicao_estrada'] == "Ruim":
                    custo *= 1.5
                heapq.heappush(fila_prioridade, (custo_acumulado + custo, vizinho, caminho_atual[:]))

    return melhor_rota


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
        duracao_segundos = rota["duracao_segundos"]
        condicao_estrada = rota["condicao_estrada"]

        if origem not in grafo:
            grafo[origem] = {}
        if destino not in grafo:
            grafo[destino] = {}

        tempo_viagem = duracao_segundos / 3600

        grafo[origem][destino] = {
            "distancia": distancia_metros / 1000,
            "tempo_viagem": tempo_viagem,
            "condicao_estrada": condicao_estrada
        }
        grafo[destino][origem] = {
            "distancia": distancia_metros / 1000,
            "tempo_viagem": tempo_viagem,
            "condicao_estrada": condicao_estrada
        }

    return grafo, cidade_origem, cidade_destino


def main():
    grafo, cidade_origem, cidade_destino = carregar_dados()
    melhor_rota = busca_custo_uniforme(grafo, cidade_origem, cidade_destino)

    if melhor_rota:
        caminho, custo = melhor_rota
        print(
            f"A melhor rota de {cidade_origem} para {cidade_destino} é: {' -> '.join(caminho)} com tempo total de {custo:.2f} horas")
    else:
        print(f"Não foi possível encontrar uma rota entre {cidade_origem} e {cidade_destino}.")


if __name__ == "__main__":
    main()