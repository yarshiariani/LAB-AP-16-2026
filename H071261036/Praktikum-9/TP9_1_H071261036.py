class Pemain:
    
    # KONSTRUKTOR 
    def __init__(self, nama, id_pemain, role, kill, assist, objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.kill = kill
        self.assist = assist
        self.objective = objective

    # MENGHITUNG SKOR
    def hitung_skor_akhir(self):
        skor = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
        return skor

    # MENENTUKAN STATUS
    def status_performa(self):
        # Memanggil method hitung_skor_akhir yang ada di atas
        skor = self.hitung_skor_akhir() 
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    # MENAMPILKAN DATA 
    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"ID Pemain: {self.id_pemain}")
        print(f"Role: {self.role}")
        print(f"Nilai Kill: {self.kill}")
        print(f"Nilai Assist: {self.assist}")
        print(f"Nilai Objective: {self.objective}")


# === PROGRAM UTAMA ===
print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

# Meminta jumlah pemain yang ingin diinput
try:
    jumlah_pemain = int(input("Masukkan jumlah pemain: "))
except ValueError:
    print("Jumlah pemain harus berupa angka!")
    exit()

daftar_pemain = []

# PERULANGAN INPUT DATA PEMAIN
for i in range(1, jumlah_pemain + 1):
    print(f"\n--- Data Pemain ke-{i} ---")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    
    try:
        kill = int(input("Nilai Kill: "))
        assist = int(input("Nilai Assist: "))
        objective = int(input("Nilai Objective: "))
    except ValueError:
        print("Nilai (Kill/Assist/Objective) harus berupa angka!")
        exit()
        
    # MENCETAK OBJEK BARU dari Class Pemain
    pemain_baru = Pemain(nama, id_pemain, role, kill, assist, objective)
    daftar_pemain.append(pemain_baru)


# TABEL REKAPITULASI
print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 76)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15} |")
print("=" * 76)

for i, p in enumerate(daftar_pemain, 1):
    skor = p.hitung_skor_akhir()
    status = p.status_performa()
    
    # Menambahkan garis '|' di awal dan akhir, serta menyesuaikan lebar kolom
    print(f"| {i:<2} | {p.nama:<10} | {p.id_pemain:<10} | {p.role:<10} | {skor:<10.2f} | {status:<15} |")
    
print("=" * 76)
