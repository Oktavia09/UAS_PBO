import networkx as nx
import matplotlib.pyplot as plt

# Data graf (peta)
peta = {
    'Badas': ['Pare', 'Kayen Kidul'],
    'Banyakan': ['Tarokan', 'Kandat'],
    'Gampengrejo': ['Pesantren', 'Grogol', 'Plemahan'],
    'Grogol': ['Ngasem', 'Gampengrejo', 'Tarokan'],
    'Gurah': ['Ngasem', 'Pare'],
    'Kandangan': ['Papar', 'Wates', 'Puncu'],
    'Kandat': ['Banyakan', 'Ringinrejo'],
    'Kayen Kidul': ['Badas', 'Plemahan'],
    'Kepung': ['Puncu', 'Ngancar'],
    'Kras': ['Ringinrejo', 'Ngadiluwih'],
    'Kunjang': ['Plosoklaten', 'Pare'],
    'Mojo': ['Ngadiluwih', 'Semen'],
    'Ngadiluwih': ['Kras', 'Mojo', 'Tarokan'],
    'Ngancar': ['Kepung', 'Plosoklaten'],
    'Ngasem': ['Grogol', 'Gurah'],
    'Pagu': ['Pare', 'Papar'],
    'Papar': ['Pare', 'Pagu', 'Kandangan'],
    'Pare': ['Plemahan', 'Badas', 'Gurah', 'Papar', 'Kunjang'],
    'Pesantren': ['Gampengrejo'],
    'Plemahan': ['Gampengrejo', 'Kayen Kidul', 'Pare'],
    'Plosoklaten': ['Ngancar', 'Kunjang'],
    'Puncu': ['Kepung', 'Kandangan'],
    'Purwoasri': ['Ringinrejo', 'Wates'],
    'Ringinrejo': ['Kandat', 'Purwoasri', 'Kras'],
    'Semen': ['Mojo'],
    'Tarokan': ['Grogol', 'Banyakan', 'Ngadiluwih'],
    'Wates': ['Kandangan', 'Purwoasri']
}

# Membuat graf dari dictionary
G = nx.Graph()

# Menambahkan simpul dan edge berdasarkan data peta
for node, neighbors in peta.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Fungsi untuk DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_result.extend(dfs(graph, neighbor, visited))
    return dfs_result

# Fungsi untuk BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    bfs_result = [start]
    
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                bfs_result.append(neighbor)
    return bfs_result

# Menjalankan DFS dan BFS
dfs_result = dfs(peta, 'Badas')
bfs_result = bfs(peta, 'Badas')

# Fungsi untuk menggambar graf dengan simpul yang dilalui oleh DFS atau BFS
def draw_graph_with_traversal(graph, traversal_result, title):
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(graph)  # Posisi simpul-simpul
    # Menentukan warna simpul yang dilalui traversal
    node_color = ['red' if node in traversal_result else 'skyblue' for node in graph.nodes]
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color=node_color, font_size=10, font_weight='bold', edge_color='gray')
    plt.title(title)
    plt.show()

# Menampilkan graf dengan hasil DFS
draw_graph_with_traversal(G, dfs_result, "Graf dengan Hasil DFS (Badas)")

# Menampilkan graf dengan hasil BFS
draw_graph_with_traversal(G, bfs_result, "Graf dengan Hasil BFS (Badas)")
