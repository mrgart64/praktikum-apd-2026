# ========================================
# Program aplikasi streaming musik ANGKASA
# ========================================

# Informasi login
nama = "Gabriel Ado Ramos Tukan"
nim = "2609106038"

# Biaya langganan senilai Rp1.500.000,00-
biaya_langganan = 1500000

# Persentase biaya administrasi paket terhadap biaya langganan
paket_orbit = 0.01 # biaya administrasi 1% untuk akses dasar ke lagu-lagu populer 
paket_nebula = 0.03 # biaya administrasi 3% untuk akses lagu premium dan playlist kustom
paket_galaxy = 0.05 # biaya administrasi 5% untuk akses lagu premium, playlist kustom, dan mode offline
paket_supernova = 0.07 # biaya administrasi 7% untuk akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis

# Input untuk login: kode warna ANSI digunakan untuk mengubah warna font atau mengubah gaya font (bold/italic) agar lebih menarik.
print ("\033[1m\033[3m=== Silakan login terlebih dahulu untuk menggunakan aplikasi streaming musik ANGKASA ===\033[0m")
input_nama = input ("Nama : ")
input_nim = input ("NIM : ")

# Validasi apakah input sesuai dengan informasi login yang ada
if input_nama == nama and input_nim == nim:
    print ("[\033[1;32m✓\033[0m] Login berhasil")
else: 
    print ("[\033[1;31mX\033[0m] Login gagal: nama atau NIM salah, tidak dapat melanjutkan program")
    exit () # Keluar jika login gagal

# Tampilan menu untuk pilih paket
print ()
print ("\033[1m\033[3m=== SILAKAN PILIH PAKET ===\033[0m")
print ("[1] Paket Orbit: akses dasar ke lagu-lagu populer (biaya administrasi 1%)")
print ("\033[0;34m[2] Paket Nebula: akses lagu premium dan playlist kustom (biaya administrasi 3%)")
print ("\033[0;33m[3] Paket Galaxy: biaya akses lagu premium, playlist kustom, dan mode offline (biaya administrasi 5%)")
print ("\033[0;31m[4] Paket Supernova: akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis (biaya administrasi 7%)\033[0m")

# Input paket berupa string digunakan dan int() tidak diperlukan agar tidak memicu error saat pengguna memasukkan huruf dan bisa langsung di-handle di bagian else
input_paket = input("Pilih paket : ")

if input_paket == "1":
    total_bayar = biaya_langganan + (biaya_langganan * paket_orbit)
elif input_paket == "2":
    total_bayar = biaya_langganan + (biaya_langganan * paket_nebula)
elif input_paket == "3":
    total_bayar = biaya_langganan + (biaya_langganan * paket_galaxy)
elif input_paket == "4":
    total_bayar = biaya_langganan + (biaya_langganan * paket_supernova)
else:
    print ("\033[1m\033[5m\033[3;31mInput tidak sesuai, coba lagi.")
    exit () # Keluar jika input tidak sesuai
    
# Tampilkan rinciannya
print ()
print ("\033[1m\033[3m=== RINCIAN BIAYA STREAMING MUSIK ANGKASA ===\033[0m")
print ("Biaya Langganan  : Rp", biaya_langganan)
print ("Total bayar      : Rp", total_bayar)
