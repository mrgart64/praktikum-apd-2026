print("ini mau saya push")

# Ini adalah contoh numerik
angka1 = 5
angka2 = 10
hasil = angka1 + angka2
print (hasil)

# Ini adalah contoh float yang biasa digunakan untuk pecahan desimal
a = 3.45
b = 1.23
hitung = a + b
print (hitung)

# Ini adalah tipe data string yang digunakan untuk menyimpan sebuah teks
name = "Gabriel"
hobi = "ngoding dan bikin web"
print (name)
print (hobi)

# Ini adalah contoh print karakter panjang
print ('''
       Saya Gabriel Ado Ramos Tukan
       Saya suka belajar coding
       Hari ini saya mengikuti praktikum coding dengan Python
       ''')

# Ini adalah contoh penggabungan teks
print ("aku""rajin""praktikum")

# Ini adalah contoh indeks string
teks = "Rahmat flowchart"
# Menampilkan indeks 3
print (teks[3])
# Menampilkan indeks 3 sampai 6
print (teks[3:6])
# Menampilkan indeks 7 sampai akhir
print (teks[7:])
# Menampilkan indeks sampai 6
print (teks[:6])
# Menampilkan indeks 1 sampai 4 dengan 2 kali step
print (teks[1:4:2])
# Menampilkan indeks -1
print (teks[-1])


# Ini adalah contoh boolean yang hanya memiliki value True atau False
Hujan = False
Panas = True

# Tipe data kolektif
biodata = ["Gabriel", 18, "2026", 89.19, True, ["APD", "26"]]
print (biodata)

# Contoh list teratur
mata_kuliah = ["APD", "Logika Matematika", "Kalkulus"]
print (mata_kuliah[0])
print (mata_kuliah[1])
print (mata_kuliah[2])

print (mata_kuliah[0:1])
print (mata_kuliah[:2])
print (mata_kuliah[1:])
print (mata_kuliah[::2])
print (mata_kuliah[:-1])

# Contoh tuple
data_mahasiswa = ("Rafi","034",True, 3.5)
print (data_mahasiswa[0])
print (data_mahasiswa[2])

# Contoh set
angka = {1, 2, 3, 4, 4, 5}
print (angka)

# Contoh dict
buku = {
'judul' : 'Atomic Habits',
'penulis' : 'James Clear',
'halaman' : 320
}

# Mengakses Value dalam Dictionary
print (buku['judul'])
print (buku['penulis'])
print (buku['halaman'])

# Mengubah string menjadi integer
angka = int ("43")
print(angka)

# Mengubah string menjadi float
ubah = float ("99.99")
print(ubah)

# Contoh input
nama = input ("Masukkan nama kamu: ")
print (nama)

gaji = int (input ("Masukkan gaji kamu: "))
print (gaji)

# Contoh operator
print (2 < 4)
print (5 > 5)

# Contoh studi kasus
jadwalZidan = {
    "pagi": "Kalkulus",
    "siang": "Algoritma Pemrograman Dasar",
    "sore": "Bahasa Inggris"
}

print (jadwalZidan["siang"])