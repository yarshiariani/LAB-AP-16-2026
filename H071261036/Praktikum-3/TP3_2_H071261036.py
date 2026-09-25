print("Setup Denah Bioskop NontonYuk")

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
        if baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
        else:
            break
    except ValueError:
        print("Input baris harus berupa angka!")

try:
    kursi = int(input("Masukkan jumlah kursi per baris: "))
    print("\nDaftar Kursi Tersedia")
    
    for i in range(1, baris + 1):
        for j in range(1, kursi + 1):
            
            # skip angka sial
            if j == 13: 
                continue
            
            # baris 1 dibikin renggang, jadi ambil ganjilnya aja (yg genap di-skip)
            if i == 1 and j % 2 == 0:
                continue
            
            print(f"Baris {i} - Kursi {j}")
            
except ValueError:
    print("Input kursi harus berupa angka!")