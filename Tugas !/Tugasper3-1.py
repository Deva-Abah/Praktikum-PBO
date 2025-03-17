from abc import ABC, abstractmethod

# Kelas abstrak Tanaman
class Tanaman(ABC):
    def __init__(self, nama, kebutuhan_air, kebutuhan_pupuk):
        self.nama = nama  # Nama tanaman
        self.kebutuhan_air = kebutuhan_air  # Kebutuhan air standar (liter)
        self.kebutuhan_pupuk = kebutuhan_pupuk  # Kebutuhan pupuk standar (kg)
    
    @abstractmethod
    def tumbuh(self):
        pass  # Metode abstrak yang harus diimplementasikan oleh subclass
    
    def hitung_kebutuhan(self, curah_hujan, kelembapan_tanah):
        # Menghitung kebutuhan air setelah mempertimbangkan curah hujan dan kelembapan tanah
        kebutuhan_air_disesuaikan = max(0, self.kebutuhan_air - curah_hujan if kelembapan_tanah > 50 else self.kebutuhan_air)
        return kebutuhan_air_disesuaikan, self.kebutuhan_pupuk
    
    def tampilkan_kebutuhan(self, curah_hujan, kelembapan_tanah):
        # Menampilkan kebutuhan air dan pupuk setelah disesuaikan dengan kondisi cuaca
        air_disesuaikan, pupuk_disesuaikan = self.hitung_kebutuhan(curah_hujan, kelembapan_tanah)
        print(f"Laporan Cuaca: Curah Hujan = {curah_hujan} mm, Kelembapan Tanah = {kelembapan_tanah}%")
        print(f"Kebutuhan Air yang Disesuaikan: {air_disesuaikan} liter" + (" (berkurang karena hujan)" if curah_hujan > 0 else ""))
        print(f"Kebutuhan Pupuk yang Disesuaikan: {pupuk_disesuaikan} kg\n")

# Kelas Padi yang merupakan turunan dari Tanaman
class Padi(Tanaman):
    def __init__(self):
        super().__init__("Padi", kebutuhan_air=20, kebutuhan_pupuk=4)  # Inisialisasi kebutuhan spesifik untuk Padi
    
    def tumbuh(self):
        print("Padi sedang tumbuh di sawah")  # Implementasi metode tumbuh

# Kelas Jagung yang merupakan turunan dari Tanaman
class Jagung(Tanaman):
    def __init__(self):
        super().__init__("Jagung", kebutuhan_air=18, kebutuhan_pupuk=7)  # Inisialisasi kebutuhan spesifik untuk Jagung
    
    def tumbuh(self):
        print("Jagung sedang tumbuh di ladang")  # Implementasi metode tumbuh

# Simulasi kondisi cuaca dan pertumbuhan tanaman
padi = Padi()
jagung = Jagung()

# Simulasi pertumbuhan tanaman dan kondisi cuaca
padi.tumbuh()
padi.tampilkan_kebutuhan(curah_hujan=10, kelembapan_tanah=75)  # Menampilkan laporan kebutuhan untuk Padi

jagung.tumbuh()
jagung.tampilkan_kebutuhan(curah_hujan=2, kelembapan_tanah=40)  # Menampilkan laporan kebutuhan untuk Jagung
