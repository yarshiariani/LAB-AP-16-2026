ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    alfabet_kecil = ALFABET
    alfabet_besar = ALFABET.upper()
    
    if ch in alfabet_kecil:
        idx = alfabet_kecil.find(ch)
        new_idx = (idx + k) % 26
        return alfabet_kecil[new_idx]
    elif ch in alfabet_besar:
        idx = alfabet_besar.find(ch)
        new_idx = (idx + k) % 26
        return alfabet_besar[new_idx]
    else:
        return ch

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        dekripsi = mesin_dekripsi(sandi, k)
        if dekripsi.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, dekripsi))
    return hasil

print("--- Hacker Caesar Cipher ---")
sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kunci = input("Masukkan kata kunci target: ")
hasil = retas_sandi(sandi, kunci)
print(f"Output Deskripsi: {hasil}")
