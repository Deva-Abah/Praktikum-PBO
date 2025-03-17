from abc import ABC, abstractmethod
import numpy as np
from sklearn.linear_model import LogisticRegression

# Kelas Induk Karyawan
class Karyawan(ABC):
    def __init__(self, nama, peran, jam_kerja, tugas_selesai):
        self.nama = nama  # Nama karyawan
        self.peran = peran  # Peran karyawan dalam perusahaan
        self.jam_kerja = jam_kerja  # Jumlah jam kerja
        self.tugas_selesai = tugas_selesai  # Jumlah tugas yang telah diselesaikan
    
    def bekerja(self):
        pass  # Metode abstrak yang harus diimplementasikan oleh kelas turunan
    
    def evaluasi_performa(self, model):
        # Menggunakan model Machine Learning untuk menentukan performa
        fitur = np.array([[self.jam_kerja, self.tugas_selesai]])  # Data input untuk prediksi
        performa = model.predict(fitur)[0]  # Melakukan prediksi performa
        return ["Performa Rendah", "Performa Sedang", "Performa Tinggi"][performa]  # Mengembalikan rating performa

# Kelas Turunan untuk berbagai jenis karyawan
class InsinyurPerangkatLunak(Karyawan):
    def bekerja(self):
        print(f"{self.nama} (Insinyur Perangkat Lunak) sedang menulis kode.")  # Aktivitas Insinyur Perangkat Lunak

class IlmuwanData(Karyawan):
    def bekerja(self):
        print(f"{self.nama} (Ilmuwan Data) sedang menganalisis data.")  # Aktivitas Ilmuwan Data

class ManajerProduk(Karyawan):
    def bekerja(self):
        print(f"{self.nama} (Manajer Produk) sedang mengelola peta jalan produk.")  # Aktivitas Manajer Produk

# Data pelatihan untuk Machine Learning (jam kerja, tugas selesai, label performa)
data = np.array([
    [40, 10, 1],  # Performa Sedang
    [35, 12, 1],  # Performa Sedang
    [50, 25, 2],  # Performa Tinggi
    [30, 5, 0],   # Performa Rendah
    [45, 20, 2],  # Performa Tinggi
    [20, 3, 0],   # Performa Rendah
    [38, 15, 1],  # Performa Sedang
    [42, 18, 1]   # Performa Sedang
])
X_train = data[:, :2]  # Fitur: jam kerja dan tugas selesai
y_train = data[:, 2]   # Label performa (0 = Rendah, 1 = Sedang, 2 = Tinggi)

# Melatih model Machine Learning
model = LogisticRegression()
model.fit(X_train, y_train)  # Model belajar dari data pelatihan

# Membuat daftar karyawan dan mengevaluasi performanya
karyawan_list = [
    InsinyurPerangkatLunak("Alice", "Insinyur Perangkat Lunak", 50, 25),
    IlmuwanData("Bob", "Ilmuwan Data", 40, 10),
    ManajerProduk("Charlie", "Manajer Produk", 38, 15),
    InsinyurPerangkatLunak("David", "Insinyur Perangkat Lunak", 30, 5)
]

for karyawan in karyawan_list:
    karyawan.bekerja()  # Menampilkan aktivitas karyawan
    print(f"Peringkat Performa: {karyawan.evaluasi_performa(model)}\n")  # Menampilkan hasil evaluasi performa