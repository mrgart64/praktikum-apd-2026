# 1.Ini adalah list harga makanan menggunakan list
harga_makanan = [15000, 16000, 19000, 20000, 21000, 22000]

# 2. Variabel NIM saya (Gabriel Ado Ramos Tukan)
nim = 38

# 3. Kurs Euro ke Rupiah
kurs_eur = 17000

# 4. Biaya aplikasi
biaya_aplikasi = 5000

# 5. Variabel makanan
makanan_1 = harga_makanan[0]
makanan_2 = harga_makanan[1]
makanan_3 = harga_makanan[2]
makanan_4 = harga_makanan[3]
makanan_5 = harga_makanan[4]
makanan_6 = harga_makanan[5]

# 6. Hitung total bayar secara manual tanpa sum()
total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + biaya_aplikasi

# 7. Hitung rata-rata
rata_rata = total_bayar / len(harga_makanan)

# 8. Variabel bolean
bolean = nim != rata_rata

# Poin Plus: Konversi total_bayar ke Euro (Asumsi kurs 1 EUR = Rp17.000)
total_bayar_eur = total_bayar / kurs_eur

# 9. Tampilkan semua variabel
print("=== RINCIAN SARAPAN MBA TAYLOR SWIFT ===")
print("Harga Makanan 1  : Rp", makanan_1)
print("Harga Makanan 2  : Rp", makanan_2)
print("Harga Makanan 3  : Rp", makanan_3)
print("Harga Makanan 4  : Rp", makanan_4)
print("Harga Makanan 5  : Rp", makanan_5)
print("Harga Makanan 6  : Rp", makanan_6)
print("Biaya Aplikasi   : Rp", biaya_aplikasi)
print("Total Bayar      : Rp", total_bayar)
print("Total Bayar (EUR):", round(total_bayar_eur, 2), "EUR")
print("Rata-rata Harga  : Rp", rata_rata)
print("2 Digit NIM      :", nim)
print("Hasil Bolean     :", bolean)

# Poin Plus: Slice dengan indeks negatif
print("=== SLICE INDEKS NEGATIF ===")
print("Makanan 1 - 6 (Indeks Negatif):", harga_makanan[-6:])