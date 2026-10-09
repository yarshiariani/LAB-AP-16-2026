def deteksi_anomali_email(email):
    error = []
    
    if email.count('@') != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error 
    
    local, domain = email.split('@')
    
    if len(local) == 0 or len(domain) == 0:
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
        
    if " " in email:
        error.append("Tidak boleh mengandung spasi di posisi manapun.")
        
    if local.startswith('.') or local.endswith('.') or '..' in local:
        error.append("Bagian local tidak boleh diawali, diakhiri titik (.), atau memiliki titik berurutan (..).")
        
    if '.' not in domain or '..' in domain or domain.endswith('.'):
        error.append("Bagian domain wajib memiliki minimal satu titik, tidak boleh mengandung titik berurutan atau diakhiri titik.")
        
    if not (email.endswith('.com') or email.endswith('.id') or email.endswith('.ac.id')):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
        
    return error

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return
        
    panjang_email = max(len(email) for email in daftar_email_valid)
    lebar_bingkai = max(panjang_email + 4, 25) 
    border_line = karakter_border * lebar_bingkai
    
    print("\n" + border_line)
    teks_tengah = " HASIL EMAIL VALID "
    sisa_spasi = lebar_bingkai - len(teks_tengah) - 2
    spasi_kiri = sisa_spasi // 2
    spasi_kanan = sisa_spasi - spasi_kiri
    print("+" + (" " * spasi_kiri) + teks_tengah + (" " * spasi_kanan) + "+")
    print(border_line)
    
    for email in daftar_email_valid:
        padding_kanan = lebar_bingkai - 4 - len(email)
        print(f"| {email}" + (" " * padding_kanan) + " |")
    print(border_line)
 
# Program Utama
print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email_input = input("Masukkan email: ")
    if email_input.lower() == 'tutup':
        break
        
    daftar_error = deteksi_anomali_email(email_input)
    
    if email_input in daftar_valid:
        print(">> Email DITOLAK karena:")
        print("Email sudah terdaftar (Duplikat).")
    elif len(daftar_error) > 0:
        print(">> Email DITOLAK karena:")
        for err in daftar_error:
            print(err)
    else:
        print(">> Email VALID!")
        daftar_valid.append(email_input)

cetak_daftar(daftar_valid, border)
