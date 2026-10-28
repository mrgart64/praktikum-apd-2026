'''
Poin (+):
- Multiuser (Admin dan Pengguna Biasa)
- Penerapan Predefined Process (Fungsi/Prosedur) pada Flowchart

Nama    : Gabriel Ado Ramos Tukan
NIM     : 2609106038

Lihat data.json untuk mendapatkat informasi login yang lebih lengkap atau lihat inforasi login di bawah ini

Login admin: {"username": "admin", "password": "Admin#1234"}

Login penerima:
[
  {"username": "067", "password": "asepasep123"},
  {"username": "068", "password": "testing67"},
  {"username": "069", "password": "barbershop66"},
  {"username": "070", "password": "gatau"},
  {"username": "306", "password": "hydrant"}
]
'''

import os
import json

# 6 variabe global digunakan
app_data = json.load(open('data.json', 'r', encoding='utf-8'))

penerima = app_data['tables']['penerima']
pengajuan = app_data['tables']['pengajuan']
blacklist = app_data['tables']['blacklist']

session = {}
is_admin = False
os.system('clear')

success_icon = '[\033[1;32m✓\033[0m]'
warning_icon = '[\033[1;33m!\033[0m]'
failed_icon = '[\033[1;31mX\033[0m]'

# 2 fungsi memakai parameter: validasiMenu(), validasiAngka()
# 2 fungsi tanpa parameter: login(), getNewData()


'''
Prosedur untuk menyimpan data
'''
def saveData():
    json.dump(app_data, open('data.json', 'w'), indent=4)

'''
Fungsi digunakan agar logika validasi menu tidak perlu diketik ulang dan lebih efisien
'''
def validasiMenu (menu, max):
    '''
    Penanganan input kosong
    '''
    if len(menu) == 0:
        print ('[\033[1;31mX\033[0m] Input harus diisi.\n')
        return False

    '''
    Poin plus: Penanganan input bukan angka dengan error handling (try/except)
    '''
    try:
        menu = int (menu) # ubah ke angka
    except:
        print ('[\033[1;31mX\033[0m] Input harus angka.\n')
        return False
    
    

    '''
    Penanganan input tidak valid
    '''
    if menu < 1 or menu > max:
        print ('[\033[1;31mX\033[0m] Input tidak valid.\n')
        return False
    
    return True

'''
Fungsi digunakan agar logika validasi angka tidak perlu diketik ulang dan lebih efisien
'''
def validasiAngka (num):
    '''
    Penanganan input kosong
    '''
    if len(num) == 0:
        print ('[\033[1;31mX\033[0m] Input harus diisi.\n')
        return False
    
    '''
    Poin plus: Penanganan input bukan angka dengan error handling (try/except)
    '''
    try:
        num = int (num) # ubah ke angka
    except:
        print ('[\033[1;31mX\033[0m] Input harus angka.\n')
        return False
    
    return True

'''
Fungsi tanpa parameter untuk login
'''
def login():
    global is_admin, penerima, session
    print('Selamat datang di aplikasi Sistem Pencatatan Rakyat Kurang Mampu dan Pembagian Sembako')
    username = input('Masukkan username Anda : ')
    password = input('Masukkan password Anda : ')
    if username == 'admin':
        if password == 'Admin#1234':
            print(f'{success_icon} Berhasil login sebagai admin')
            is_admin = True
            return True
        else:
            print('[X] Password admin salah.')
            return False
    else:
        for i in penerima.values():
            print(i)
            if username == i['nik']:
                if password == i['password']:
                    print(f'{success_icon} Berhasil login sebagai {i['nama']}')
                    session = i
                    return True
                else:
                    print(f'{failed_icon} Password pengguna salah.')
                    return False
        
        print(f'{failed_icon} Pengguna tidak ditemukan.')
        return False

'''
Prosedur adminTambahPenerima() dengan 1 global variable dan 4 local variables
'''
def adminTambahPenerima():
    global penerima
    print('=== Tambah Penerima ==')
    nama = input('Masukkan nama : ')
    nik = input('Masukkan nik : ')
    if not validasiAngka(nik):
        return
    alamat = input('Masukkan alamat : ')
    password = input('Masukkan password : ')
    penerima[nik] = {'nik': nik, 'nama': nama, 'alamat': alamat, 'password': password}
    saveData()
    print('Penerima berhasil dibuat')
    
'''
Prosedur adminLihatPenerima() dengan 1 global variable dan 2 local variables
'''
def adminLihatPenerima():
    global penerima
    print('=== Lihat Semua Penerima ==')
    j = 1
    for i in penerima.values():
        print(f'[{j}] {i['nik']} | {i['nama']} | {i['alamat']}')
        j += 1
        
'''
Prosedur adminUbahStatus() dengan 1 global variable dan beberapa local variables
'''
def adminUbahStatus():
    global penerima, pengajuan, blacklist
    print('=== Ubah Status Pengajuan ==')
    print('Pilih penerima yang akan diubah statusnya')
    pengajuan_menu = []
    for i in penerima.values():
        if pengajuan.get(i['nik']):
            if pengajuan[i['nik']]['status'] == 'menunggu persetujuan':
                pengajuan_menu.append({'nik': i['nik'], 'nama': i['nama'], 'alamat': i['alamat'], 'status': pengajuan[i['nik']]['status'], 'desc': pengajuan[i['nik']]['desc']})
                print(f'[{len(pengajuan_menu)}] {pengajuan_menu[len(pengajuan_menu)-1]['nik']} | {pengajuan_menu[len(pengajuan_menu)-1]['nama']} | {pengajuan_menu[len(pengajuan_menu)-1]['alamat']}')
                
    selected = pengajuan_menu[int(input('Pilih calon penerima yang akan disetujui : '))-1]
    
    os.system('clear')
    
    print('=== Informasi Penerima ==')
    print(f'NIK                  : {selected['nik']}')
    print(f'Nama                 : {selected['nama']}')
    print(f'Alamat               : {selected['alamat']}')
    print(f'Status pengajuan     : {selected['status']}')
    print(f'Alasan pengajuan     : \n{selected['desc']}')
    
    print('=== Menu ===')
    print('[1] Setujui')
    print('[2] Tolak')
    print('[3] Blokir')
    print('[4] Keluar')
    
    select_menu = int(input('Pilih menu : '))
    
    if select_menu == 1:
        pengajuan[selected['nik']]['status'] = 'disetujui'
        saveData()
        print('Pengajuan berhasil disetujui')
    elif select_menu == 2:
        # desc = input('Masukkan alasan penolakan pengajuan : ')
        pengajuan[selected['nik']]['status'] = 'ditolak'
        saveData()
        print('Pengajuan berhasil ditolak')
    elif select_menu == 3:
        desc = input('Masukkan alasan pemblokiran : ')
        pengajuan[selected['nik']]['status'] = 'ditolak'
        blacklist[selected['nik']] = { 'desc': desc}
        saveData()
        print('Penerima berhasil diblokir')
    else:
        print('Dibatalkan')

'''
Fungsi tanpa parameter getNewData() dengan 1 global variable dan beberapa global variables
'''
def getNewData():
    global penerima
    print('=== Ubah Penerima ==')
    j = 1
    for i in penerima.values():
        print(f'[{j}] {i['nik']} | {i['nama']} | {i['alamat']}')
        j += 1
        
    index = int(input('pilih penerima : '))-1
    nama = input('Masukkan nama : ')
    alamat = input('Masukkan alamat : ')
    
    return (index, nama, alamat)

'''
Prosedur adminUbahPenerima() dengan 1 global variable dan beberapa local variables
'''
def adminUbahPenerima():
    global penerima
    (index, nama, alamat) = getNewData()
    keys = list(penerima.keys())
    penerima[keys[index]] = {'nik': keys[index], 'nama': nama, 'alamat': alamat, 'password': penerima[keys[index]]['password']}
    saveData()
    print('Data penerima berhasil diubah')

'''
Prosedur adminHapusPenerima() dengan 3 global variables dan beberapa local variables
'''
def adminHapusPenerima():
    global penerima, blacklist, pengajuan
    print('=== Hapus Penerima ==')
    j = 1
    for i in penerima.values():
        print(f'[{j}] {i['nik']} | {i['nama']} | {i['alamat']}')
        j += 1
        
    index = int(input('pilih penerima yang akan dihapus : '))-1
    deleted = penerima.pop(list(penerima.keys())[index])
    if blacklist.get(deleted['nik']):
        blacklist.pop(deleted['nik'])
    if pengajuan.get(deleted['nik']):
        pengajuan.pop(deleted['nik'])
    saveData()
    print(f'{deleted['nama']} ({deleted['nik']}) berhasil dihapus')
    
'''
Prosedur userBuatPengajuan() dengan 2 global variables dan beberapa local variables
'''
def userBuatPengajuan():
    global blacklist, pengajuan
    if blacklist.get(session['nik']):
        print('Akun Anda terblokir atau kena banned, silakan datangi kantor program sembako secara offline untuk verifikasi dan klarifikasi lebih lanjut.')
        return
    
    if pengajuan.get(session['nik']):
        if pengajuan.get(session['nik'])['status'] == 'menunggu persetujuan':
            print('Anda telah mengirim pengajuan sembako dan petugas akan memverifikasi lebih lanjut\ndalam waktu beberapa minggu sampai beberapa bulan sesuai regulasi dan birokrasi\nmasing-masing wilayah regoinal.')
            return
    
    desc = input('Masukkan alasan pengajuan : ')
    pengajuan[session['nik']] = {'desc': desc, 'status': 'menunggu persetujuan'}
    saveData()
    print('Pengajuan berhasil dibuat.')
    
    
'''
Prosedur userLihatStatus() dengan 2 global variables dan beberapa local variable
'''
def userLihatStatus():
    global pengajuan, blacklist
    if not pengajuan.get(session['nik']):
        print('Anda belum membuat pengajuan.')
        return
    
    kena_banned = blacklist.get(session['nik'])
    
    print('=== STATUS PENGAJUAN ===')
    print('Proses verifikasi mungkin memakan waktu beberapa minggu sampai\nbeberapa bulan bergantung pada regulasi dan birokrasi masing-masing wilayah regional.')
    print('[!] Cek secara berkala status pengajuan di aplikasi ini.\n')
    print(f'Status pengajuan : {pengajuan[session['nik']]['status']}')
    print(f'Deskripsi pengajuan \n{pengajuan[session['nik']]['desc']}\n')
    
    if pengajuan[session['nik']]['status'] == 'disetujui':
        print('Selamat, Anda telah terverifikasi sebagai penerima, Anda berhak mendapatkan sembako.\n')
        
    if pengajuan[session['nik']]['status'] == 'ditolak' and kena_banned:
        print('Akun Anda terkena banned, Anda tidak dapat membuat\nulang pengajuan dan Anda tidak berhak mendapatkan sembako.\nSilakan datangi kantor pembagian sembako untuk verifikasi data dan klarifikasi\nlalu Anda membuat kembali pengajuan melalui aplikasi ini dan melewati prosedur birokasi sesuai protokol')
    
    if pengajuan[session['nik']]['status'] == 'ditolak' and not kena_banned:
        print('Pengajuan ditolak, Anda dapat membuat ulang pengajuan dan\nkembali melewati prosedur birokasi sesuai protokol')
    
    if kena_banned:
        print(f'Status akun : TIDAK SEHAT / KENA BANNED {failed_icon}')
        print(f'{warning_icon} Akun Anda terkena banned')
        print(f'Alasan pemblokiran: \n{blacklist[session['nik']]['desc']}')
    else:
        print(f'Status akun : SEHAT {success_icon}')

'''
Prosedur menu admin
'''
def adminMenu():
    print('=== Admin Menu ==')
    print('[1] Tambah penerima      | CREATE')
    print('[2] Lihat penerima       | READ')
    print('[3] Setujui pengajuan    | UPDATE')
    print('[4] Ubah data penerima   | UPDATE')
    print('[5] Hapus penerima       | DELETE')
    print('[6] Keluar')
    menu = input('Pilih menu : ')
    os.system('clear')
    if not validasiMenu(menu, 6):
        return
    
    menu = int(menu)
    
    if menu == 1:
        adminTambahPenerima()
    elif menu == 2:
        adminLihatPenerima()
    elif menu == 3:
        adminUbahStatus()
    elif menu == 4:
        adminUbahPenerima()
    elif menu == 5:
        adminHapusPenerima()
    elif menu == 6:
        exit()

'''
Prosedur menu pengguna biasa
'''
def userMenu():
    print('=== User Menu ===')
    print('PERHATIAN: Proses verifikasi mungkin memakan waktu beberapa minggu sampai\nbeberapa bulan bergantung pada regulasi dan birokrasi masing-masing wilayah regional.\nDatangi kantor program sembako secara offline untuk verifikasi dan klarifikasi lebih lanjut jika akun Anda terblokir.\nPilih menu : ')
    print('[1] Buat pengajuan   | CREATE')
    print('[2] Lihat status     | READ')
    print('[3] Keluar')
    menu = input('Pilih menu : ')
    os.system('clear')
    if not validasiMenu(menu, 6):
        return
    
    menu = int(menu)
    
    if menu == 1:
        userBuatPengajuan()
    elif menu == 2:
        userLihatStatus()
    elif menu == 3:
        exit()

'''
Prosedur menu
'''
def mainMenu():
    while (1):
        os.system('clear')
        print('Sistem Pencatatan Rakyat Kurang Mampu dan Pembagian Sembako')
        print('"Kami berkomitmen untuk membagikan karbohidrat secara gratis"')
        if is_admin:
            adminMenu()
        else:
            userMenu()
        input('\nTekan enter untuk melanjutkan...\n')


def main():
    while True:
        if login():
            break
        
    mainMenu()
    
main()