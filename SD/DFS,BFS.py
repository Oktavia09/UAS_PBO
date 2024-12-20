# Representasi graf menggunakan dictionary untuk wilayah Kabupaten Kediri
# Menambahkan 'Pesantren' sebagai simpul dalam graf
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
    'Pesantren': ['Gampengrejo'],  # Menambahkan simpul Pesantren
    'Plemahan': ['Gampengrejo', 'Kayen Kidul', 'Pare'],
    'Plosoklaten': ['Ngancar', 'Kunjang'],
    'Puncu': ['Kepung', 'Kandangan'],
    'Purwoasri': ['Ringinrejo', 'Wates'],
    'Ringinrejo': ['Kandat', 'Purwoasri', 'Kras'],
    'Semen': ['Mojo'],
    'Tarokan': ['Grogol', 'Banyakan', 'Ngadiluwih'],
    'Wates': ['Kandangan', 'Purwoasri']
}


# Implementasi DFS
def dfs(graph, start, visited=None):
    """
    Depth-First Search (DFS) untuk menelusuri graf secara rekursif.
    :param graph: Dictionary yang merepresentasikan graf.
    :param start: Simpul awal untuk memulai DFS.
    :param visited: Set untuk menyimpan simpul yang sudah dikunjungi.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Implementasi BFS
def bfs(graph, start):
    """
    Breadth-First Search (BFS) untuk menelusuri graf secara iteratif.
    :param graph: Dictionary yang merepresentasikan graf.
    :param start: Simpul awal untuk memulai BFS.
    """
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Uji coba traversal graf menggunakan DFS dan BFS
if __name__ == "__main__":
    print("Traversal DFS dari simpul Badas:")
    dfs(peta, 'Badas')
    print("\n")

    print("Traversal BFS dari simpul Badas:")
    bfs(peta, 'Badas')


