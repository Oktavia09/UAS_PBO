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

# Menggambar graf
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)  # Posisi simpul-simpul
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title('Graf Wilayah Kabupaten Kediri')
plt.show()
