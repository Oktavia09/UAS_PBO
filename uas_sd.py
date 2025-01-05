import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import radians, sin, cos, sqrt, atan2

class AplikasiVisualisasiRute:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualisasi Rute Kediri")
        self.root.geometry("1200x800")
        
        # Membuat frame utama
        self.frame_kontrol = ttk.Frame(root, padding="10")
        self.frame_kontrol.pack(fill=tk.X)
        
        self.frame_peta = ttk.Frame(root)
        self.frame_peta.pack(fill=tk.BOTH, expand=True)
        
        # Membuat kontrol input
        self.buat_kontrol()
        
        # Inisialisasi peta
        self.buat_peta()
        
        # Gambar awal
        self.perbarui_peta()

    def buat_kontrol(self):
        # Pemilihan lokasi
        ttk.Label(self.frame_kontrol, text="Lokasi Awal:").pack(side=tk.LEFT, padx=5)
        self.var_awal = tk.StringVar()
        self.combo_awal = ttk.Combobox(self.frame_kontrol, textvariable=self.var_awal)
        self.combo_awal['values'] = list(koordinat.keys())
        self.combo_awal.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(self.frame_kontrol, text="Lokasi Tujuan:").pack(side=tk.LEFT, padx=5)
        self.var_tujuan = tk.StringVar()
        self.combo_tujuan = ttk.Combobox(self.frame_kontrol, textvariable=self.var_tujuan)
        self.combo_tujuan['values'] = list(koordinat.keys())
        self.combo_tujuan.pack(side=tk.LEFT, padx=5)
        
        # Tombol hitung
        self.tombol_hitung = ttk.Button(self.frame_kontrol, text="Hitung Rute", 
                                    command=self.hitung_rute)
        self.tombol_hitung.pack(side=tk.LEFT, padx=20)
        
        # Tampilan hasil
        self.label_hasil = ttk.Label(self.frame_kontrol, text="")
        self.label_hasil.pack(side=tk.LEFT, padx=5)

    def buat_peta(self):
        self.gambar, self.ax = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.gambar, master=self.frame_peta)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def perbarui_peta(self, jalur=None):
        self.ax.clear()
        
        # Membuat graf
        G = nx.Graph()
        for simpul, tetangga in peta.items():
            for tujuan in tetangga:
                G.add_edge(simpul, tujuan)
        
        # Ekstrak koordinat untuk plotting
        posisi = {simpul: (koord[1], koord[0]) for simpul, koord in koordinat.items()}
        
        # Gambar semua edge dengan warna abu-abu muda
        nx.draw_networkx_edges(G, posisi, edge_color='lightgray', width=1)
        
        # Gambar jalur yang dipilih jika ada
        if jalur:
            edge_jalur = list(zip(jalur[:-1], jalur[1:]))
            nx.draw_networkx_edges(G, posisi, edgelist=edge_jalur, 
                                 edge_color='red', width=2)
        
        # Gambar simpul
        nx.draw_networkx_nodes(G, posisi, node_color='skyblue', 
                             node_size=500)
        
        # Gambar label
        nx.draw_networkx_labels(G, posisi, font_size=8)
        
        # Atur batas peta
        self.ax.set_title("Peta Rute Wilayah Kediri")
        plt.axis('on')
        self.canvas.draw()

    def hitung_rute(self):
        awal = self.var_awal.get()
        tujuan = self.var_tujuan.get()
        
        if not awal or not tujuan:
            self.label_hasil.config(text="Silakan pilih lokasi awal dan tujuan")
            return
        
        hasil = cari_jarak_jalur(awal, tujuan)
        
        if isinstance(hasil, dict):
            teks_hasil = f"Jarak: {hasil['total_jarak']} km"
            self.label_hasil.config(text=teks_hasil)
            self.perbarui_peta(hasil['jalur'])
        else:
            self.label_hasil.config(text=hasil)
            self.perbarui_peta()

koordinat = {
    'Badas': (-7.7024, 112.210324),
    'Pare': (-7.744221, 112.198385),
    'Kayen Kidul': (-7.729369, 112.117898),
    'Banyakan': (-7.767142, 111.983182),
    'Tarokan': (-7.709625, 111.936062),
    'Kandat': (-7.903422,112.033264),
    'Gampengrejo': (-7.636162,112.014221),
    'Grogol': (-7.743048,111.961727),
    'Plemahan': (-7.723048,112.142234),
    'Ngasem': (-7.8089841,112.038759),
    'Gurah': (-7.805475,112.103961),
    'Kandangan': (-7.755520,112.286962),
    'Papar': (-7.698315,112.081304),
    'Wates': (-7.915919,112.126827),
    'Puncu': (-7.843338,112.229912),
    'Ringinrejo': (-7.978624,112.030897),
    'Kepung': (-7.815780,112.294695),
    'Ngancar': (-7.936003,112.195312),
    'Kras': (-7.953000, 111.960047),
    'Ngadiluwih': (-7.898974,112.013092),
    'Mojo': (-7.873544,111.836765),
    'Semen': (-7.824647,111.936875),
    'Kunjang': (-7.672429,112.186408),
    'Plosoklaten': (-7.879009,112.151029),
    'Pagu': (-7.787449,112.075877),
    'Purwoasri': (-7.638565,112.125895)
}

def hitung_jarak(koord1, koord2):
    R = 6371  # Radius bumi dalam kilometer
    
    lat1, lon1 = koord1
    lat2, lon2 = koord2
    
    # Konversi koordinat ke radian
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Perbedaan koordinat
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Rumus haversine
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    jarak = R * c
    
    return round(jarak, 2)

def cari_jarak_jalur(awal, tujuan):
    if awal not in koordinat or tujuan not in koordinat:
        return "Satu atau kedua lokasi tidak ditemukan dalam database koordinat."
    
    # Membuat graf dengan bobot berdasarkan jarak aktual
    G = nx.Graph()
    
    # Tambahkan edge dengan bobot berdasarkan jarak
    for simpul, tetangga in peta.items():
        for tujuan_tetangga in tetangga:
            jarak = hitung_jarak(koordinat[simpul], koordinat[tujuan_tetangga])
            G.add_edge(simpul, tujuan_tetangga, weight=jarak)
    
    try:
        # Mencari jalur terpendek
        jalur = nx.shortest_path(G, awal, tujuan, weight='weight')
        total_jarak = 0
        
        # Hitung total jarak
        for i in range(len(jalur)-1):
            total_jarak += hitung_jarak(koordinat[jalur[i]], koordinat[jalur[i+1]])
        
        return {
            'jalur': jalur,
            'total_jarak': round(total_jarak, 2),
            'jarak_langsung': hitung_jarak(koordinat[awal], koordinat[tujuan])
        }
    except nx.NetworkXNoPath:
        return "Tidak ditemukan jalur antara kedua lokasi."

# Dictionary peta tetap sama
peta = {
    'Badas': ['Pare', 'Kandangan','Plemahan','Kunjang','Kepung'],
    'Banyakan': ['Mojo','Semen','Grogol','Gampengrejo'],
    'Gampengrejo': ['Banyakan','Ngasem','Pagu', 'Kayen Kidul'],
    'Grogol': ['Banyakan', 'Gampengrejo', 'Tarokan'],
    'Gurah': ['Ngasem', 'Pagu','Kayen Kidul','Pare','Plosoklaten','Wates'],
    'Kandangan': ['Badas','Kepung'],
    'Kandat': ['Ngadiluwih','Kras','Ringinrejo','Wates'],
    'Kayen Kidul': ['Gampengrejo','Gurah','Pare', 'Plemahan','Papar','Pagu'],
    'Kepung': ['Puncu', 'Pare','Badas','Kandangan'],
    'Kras': ['Ringinrejo', 'Ngadiluwih','Kandat','Mojo'],
    'Kunjang': ['Purwoasri','Plemahan','Badas'],
    'Mojo': ['Ngadiluwih', 'Semen','Kras','Banyakan'],
    'Ngadiluwih': ['Kras', 'Mojo', 'Kandat'],
    'Ngancar': ['Ringinrejo','Wates', 'Plosoklaten','Puncu'],
    'Ngasem': ['Gampengrejo', 'Gurah','Pagu'],
    'Pagu': ['Ngasem','Pare', 'Gampengrejo','Kayen Kidul','Gurah'],
    'Papar': ['Kayen Kidul','Plemahan','Purwoasri'],
    'Pare': ['Plemahan', 'Badas', 'Gurah', 'Kepung', 'Plosoklaten','Puncu','Kayen Kidul'],   
    'Plemahan': ['Purwoasri', 'Kayen Kidul', 'Pare','Badas','Kunjang','Papar'],
    'Plosoklaten': ['Ngancar', 'Wates','Gurah','Pare','Puncu'],
    'Puncu': ['Kepung', 'Ngancar','Plosoklaten','Pare'],
    'Purwoasri': ['Kunjang','Plemahan','Papar'],
    'Ringinrejo': ['Kandat', 'Wates', 'Kras','Ngancar'],
    'Semen': ['Mojo','Banyakan'],
    'Tarokan': ['Grogol'],
    'Wates': ['Kandat','Ringinrejo','Gurah','Ngancar','Plosoklaten',]
}

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiVisualisasiRute(root)
    root.mainloop()