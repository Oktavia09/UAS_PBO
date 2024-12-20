import heapq
import sys

def dijkstra(graph, start):
    # Inisialisasi jarak dengan nilai tak hingga
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    
    # Priority queue untuk menyimpan pasangan (jarak, node)
    pq = [(0, start)]
    
    # Untuk melacak jalur terpendek
    previous_nodes = {node: None for node in graph}
    
    while pq:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)
        
        # Jika jarak saat ini lebih besar dari yang tersimpan, lewati
        if current_distance > distances[current_node]:
            continue
        
        # Periksa tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika jalur baru lebih pendek, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous_nodes

# Contoh graf menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3},
    'C': {'B': 1, 'D': 5},
    'D': {}
}

# Jalankan algoritma dari node A
shortest_distances, path_tracking = dijkstra(graph, 'A')

print("Jarak Terpendek dari A:")
for node, distance in shortest_distances.items():
    print(f"A ke {node}: {distance}")

# Fungsi untuk merekonstruksi jalur terpendek
def get_path(previous_nodes, start, end):
    path = []
    current_node = end
    
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    
    path.reverse()
    return path

# Contoh mendapatkan jalur terpendek dari A ke D
path_to_d = get_path(path_tracking, 'A', 'D')
print("\nJalur Terpendek A ke D:", ' -> '.join(path_to_d))