import osmnx as ox
import json
import matplotlib.pyplot as plt
import re
import os
import glob

# Configurar o OSMnx para evitar caches ou salvamento de dados extras
ox.settings.use_cache = False  # Desativa o cache do OSMnx
ox.settings.log_file = False  # Desativa logs em arquivo
ox.settings.log_console = False  # Exibe logs no console para depuração

# Definir o local (bairro específico)
place_name = "Redonda, Teresina, Piauí, Brazil"

# Função para criar um nome de arquivo seguro a partir do endereço
def create_safe_filename(place_name):
    # Remover caracteres especiais e substituir espaços/vírgulas por sublinhados
    safe_name = re.sub(r'[^\w\s,-]', '', place_name)  # Remove caracteres especiais
    safe_name = safe_name.replace(' ', '_').replace(',', '_').replace('-', '_')
    return safe_name

# Definir a pasta principal e a subpasta
cache_dir = "cache"
sub_dir_name = create_safe_filename(place_name)
output_dir = os.path.join(cache_dir, sub_dir_name)

# Criar a pasta de destino (cache e subpasta) se não existirem
os.makedirs(output_dir, exist_ok=True)

# Listar e remover arquivos JSON e PNG existentes na pasta de destino
print("Arquivos na pasta antes da execução:")
for file in glob.glob(os.path.join(output_dir, "*")):
    print(f"- {file}")
    if file.endswith(".json") or file.endswith(".png"):
        os.remove(file)
        print(f"Removido arquivo antigo: {file}")

# Gerar nome base para os arquivos
file_base_name = create_safe_filename(place_name)

# Baixar o grafo de ruas (somente para veículos)
graph = ox.graph_from_place(place_name, network_type="drive")

# Função para converter o grafo em JSON
def graph_to_json(graph):
    nodes = []
    edges = []

    # Extrair nós (interseções)
    for node, data in graph.nodes(data=True):
        nodes.append({
            "id": str(node),
            "latitude": data["y"],
            "longitude": data["x"]
        })

    # Extrair arestas (ruas)
    for u, v, key, data in graph.edges(keys=True, data=True):
        # Tratando o maxspeed
        maxspeed = data.get("maxspeed", 50)  # Se não tiver, assume 50 km/h
        if isinstance(maxspeed, list):
            maxspeed = maxspeed[0]  # Se for lista, pega o primeiro valor
        try:
            maxspeed = float(maxspeed)  # Converte para número se possível
        except:
            maxspeed = 50  # Se der erro, assume 50

        edges.append({
            "id": f"{u}-{v}-{key}",
            "source": str(u),
            "target": str(v),
            "length": data.get("length", 0.0),  # Comprimento em metros
            "travel_time": 0.0,  # Será calculado no Java
            "oneway": data.get("oneway", False),
            "maxspeed": maxspeed
        })

    return {"nodes": nodes, "edges": edges}

# Converter grafo para JSON
graph_json = graph_to_json(graph)

# Salvar como arquivo JSON na pasta especificada
json_filename = os.path.join(output_dir, f"{file_base_name}.json")
with open(json_filename, "w") as f:
    json.dump(graph_json, f, indent=2)

# Visualizar o grafo
fig, ax = ox.plot_graph(graph, node_size=10, edge_color="blue", edge_linewidth=1, show=False, close=False)

# Salvar a imagem do grafo na pasta especificada
image_filename = os.path.join(output_dir, f"{file_base_name}.png")
plt.savefig(image_filename, dpi=300, bbox_inches="tight")
plt.close(fig)  # Fechar a figura para evitar consumo de memória

# Listar arquivos na pasta após a execução para verificar se há arquivos indesejados
print("Arquivos na pasta após a execução:")
for file in glob.glob(os.path.join(output_dir, "*")):
    print(f"- {file}")

print(f"Arquivo JSON salvo como '{json_filename}'.")
print(f"Imagem do grafo salva como '{image_filename}'.")