# Roteamento de Entregas de Produtos Perecíveis (Grupo 3)
## Descrição
A empresa BdR precisa planear o trajeto ideal para uma frota de caminhões que entrega produtos perecíveis a
supermercados em Moçambique. As entregas devem ser feitas no menor tempo possível, evitando
congestionamentos e estradas em más condições. O problema envolve cidades Moçambicanas interligadas por
estradas com custos variados (tempo e distância), e a solução deve garantir que as mercadorias sejam entregues
dentro do prazo.

## Membros do Grupo
- Amosse Nhambombe
- Clifton Da Fonseca
- Isidro Bata
- José Matimbe

## Requisitos
- Python 3.8 ou superior
- pip
- Api Key do OpenRouteService

## Instalação
1. Clone o repositório
```bash
  git clone https://github.com/kiddingmz/IA1_Trabalho.git
```

2. Crie um ambiente virtual
```bash
  python -m venv venv
```

3. Ative o ambiente virtual
```bash
  source venv/bin/activate
```

4. Instale as dependências
```bash
  pip install -r requirements.txt
```

## Execução
```bash
  python main.py
```

## Testes
```bash
  python -m doctest -v tests/<nome_do_arquivo>.txt
```