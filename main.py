#!/usr/bin/env python3
def busca_a_estrela():
    import algoritmos.busca_a_estrela as busca_a_estrela
    busca_a_estrela.main()


def busca_custo_uniforme():
    import algoritmos.busca_custo_uniforme as busca_custo_uniforme
    busca_custo_uniforme.main()


def busca_largura():
    import algoritmos.busca_largura as busca_largura
    busca_largura.main()


def busca_profundidade_iterativa():
    import algoritmos.busca_profundidade_iterativa as busca_profundidade_iterativa
    busca_profundidade_iterativa.main()


def gerar_grafo():
    import utils.gerar_grafo as gerar_grafo
    gerar_grafo.main()


def inserir_dados():
    import utils.heuristica as inserir_dados
    inserir_dados.main()


def menu_novos_dados():
    nova_entrada = input("Deseja inserir novos dados? (s/n): ").lower()
    if nova_entrada == "s":
        inserir_dados()


def mostrar_menu():
    print("\nMenu Principal:")
    print("1. Inserir novos dados")
    print("2. Busca A*")
    print("3. Busca Custo Uniforme")
    print("4. Busca em Largura")
    print("5. Busca Profundidade Iterativa")
    print("6. Ver Grafo das cidades")
    print("0. Sair")


def main():
    inserir_dados()

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_novos_dados()
        if escolha == "2":
            busca_a_estrela()
        elif escolha == "3":
            busca_custo_uniforme()
        elif escolha == "4":
            busca_largura()
        elif escolha == "5":
            busca_profundidade_iterativa()
        elif escolha == "6":
            gerar_grafo()
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
