import json
import os

import networkx as nx
import matplotlib.pyplot as plt


def main():
    with open(os.path.join(os.path.dirname(__file__), '../data/rotas_detalhadas.json'), 'r') as file:
        rotas_detalhadas = json.load(file)

    G = nx.Graph()

    for rota in rotas_detalhadas:
        origem = rota['origem']
        destino = rota['destino']
        distancia = rota['distancia_metros']

        if origem not in G:
            G.add_node(origem)
        if destino not in G:
            G.add_node(destino)

        G.add_edge(origem, destino, distancia=distancia)

    plt.figure(figsize=(35, 25))

    pos = nx.kamada_kawai_layout(G)

    nx.draw(G, pos, with_labels=True, node_size=4500, node_color='skyblue', font_size=14, font_weight='bold',
            edge_color='gray', width=3)

    edge_labels = {(origem, destino): f"{d['distancia']} m"
                   for origem, destino, d in G.edges(data=True)}

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14)
    plt.show()


if __name__ == "__main__":
    main()
