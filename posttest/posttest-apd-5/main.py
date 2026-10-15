'''
Poin (+):
- Multiuser (Admin dan Pengguna Biasa)
- Dapat melakukan Register
- Error Handling (Tidak menggunakan Try dan Except)
- Menggunakan Nested List
- Menggunakan Clear Terminal dengan import os
'''

import os
import json

app_data = json.load(open('data.json', 'r', encoding='utf-8'))

penerima = app_data['tables']['penerima']
pengajuan = app_data['tables']['pengajuan']
blacklist = app_data['tables']['blacklist']

session = {}
is_admin = False

os.system('clear')
print('Selamat datang di aplikasi Sistem Pencatatan Rakyat Kurang Mampu dan Pembagian Sembako')
username = input('Masukkan username Anda : ')
password = input('Masukkan password Anda : ')

loop = True
while(loop):
    if username == 'admin':
        if password == 'Admin#1234':
            print('[V] Berhasil login sebagai admin')
            is_admin = True
            loop = False
        else:
            print('[X] Password admin salah.')
    else:
        for i in penerima.values():
            if username == i['nik']:
                if password == i['password']:
                    print(f'[V] Berhasil login sebagai {i['nama']}')
                    session = i
                    loop = False
                    break
                else:
                    print('[X] Password pengguna salah.')
            else:
                print('[X] Pengguna tidak ditemukan.')

while (1):
    os.system('clear')
    print('Sistem Pencatatan Rakyat Kurang Mampu dan Pembagian Sembako')
    print('"Kami berkomitmen untuk membagikan karbohidrat secara gratis"')
    if is_admin:
        print('=== Admin Menu ==')
        print('[1] Tambah penerima      | CREATE')
        print('[2] Lihat penerima       | READ')
        print('[3] Setujui pengajuan    | UPDATE')
        print('[4] Ubah data penerima   | UPDATE')
        print('[5] Hapus penerima       | DELETE')
        print('[6] Keluar')
        menu = int(input('Pilih menu : '))
        
        if menu == 1:
            os.system('clear')
            print('=== Tambah Penerima ==')
            nama = input('Masukkan nama : ')
            nik = input('Masukkan nik : ')
            alamat = input('Masukkan alamat : ')
            password = input('Masukkan password : ')
            penerima[nik] = {'nik': nik, 'nama': nama, 'alamat': alamat, 'password': password}
            json.dump(app_data, open('data.json', 'w'), indent=4)
            print('Penerima berhasil dibuat')
            input('\nTekan enter untuk melanjutkan...\n')
        elif menu == 2:
            os.system('clear')
            print('=== Lihat Semua Penerima ==')
            j = 1
            for i in penerima.values():
                print(f'[{j}] {i['nik']} | {i['nama']} | {i['alamat']}')
                j += 1
            input('\nTekan enter untuk melanjutkan...\n')
        elif menu == 3:
            os.system('clear')
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
                json.dump(app_data, open('data.json', 'w'), indent=4)
                print('Pengajuan berhasil disetujui')
            elif select_menu == 2:
                # desc = input('Masukkan alasan penolakan pengajuan : ')
                pengajuan[selected['nik']]['status'] = 'ditolak'
                json.dump(app_data, open('data.json', 'w'), indent=4)
                print('Pengajuan berhasil ditolak')
            elif select_menu == 3:
                desc = input('Masukkan alasan pemblokiran : ')
                pengajuan[selected['nik']]['status'] = 'ditolak'
                blacklist[selected['nik']] = { 'desc': desc}
                json.dump(app_data, open('data.json', 'w'), indent=4)
                print('Penerima berhasil diblokir')
            else:
                print('Dibatalkan')
                continue
            
            input('\nTekan enter untuk melanjutkan...\n')
            
        elif menu == 4:
            os.system('clear')
            print('=== Ubah Penerima ==')
            j = 1
            for i in penerima.values():
                print(f'[{j}] {i['nik']} | {i['nama']} | {i['alamat']}')
                j += 1
                
            index = int(input('pilih penerima : '))-1
            nama = input('Masukkan nama : ')
            alamat = input('Masukkan alamat : ')
            test = {}
            keys = list(penerima.keys())
            penerima[keys[index]] = {'nik': keys[index], 'nama': nama, 'alamat': alamat, 'password': penerima[keys[index]]['password']}
            json.dump(app_data, open('data.json', 'w'), indent=4)
            print('Data penerima berhasil diubah')
            input('\nTekan enter untuk melanjutkan...\n')
        elif menu == 5:
            os.system('clear')
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
            json.dump(app_data, open('data.json', 'w'), indent=4)
            print(f'{deleted['nama']} ({deleted['nik']}) berhasil dihapus')
            input('\nTekan enter untuk melanjutkan...\n')
        elif menu == 6:
            exit()
            
    else:
        print('=== User Menu ===')
        print('PERHATIAN: Proses verifikasi mungkin memakan waktu beberapa minggu sampai\nbeberapa bulan bergantung pada regulasi dan birokrasi masing-masing wilayah regional.\nDatangi kantor program sembako secara offline untuk verifikasi dan klarifikasi lebih lanjut jika akun Anda terblokir.\nPilih menu : ')
        print('[1] Buat pengajuan   | CREATE')
        print('[2] Lihat status     | READ')
        print('[3] Keluar')
        menu = int(input('Pilih menu : '))
        
        if menu == 1:
            os.system('clear')
            if blacklist.get(session['nik']):
                print('Akun Anda terblokir atau kena banned, silakan datangi kantor program sembako secara offline untuk verifikasi dan klarifikasi lebih lanjut.')
                input('\nTekan enter untuk melanjutkan...\n')
                continue
            
            if pengajuan.get(session['nik']):
                if pengajuan.get(session['nik'])['status'] == 'menunggu persetujuan':
                    print('Anda telah mengirim pengajuan sembako dan petugas akan memverifikasi lebih lanjut\ndalam waktu beberapa minggu sampai beberapa bulan sesuai regulasi dan birokrasi\nmasing-masing wilayah regoinal.')
                    input('\nTekan enter untuk melanjutkan...\n')
                    continue
            
            desc = input('Masukkan alasan pengajuan : ')
            pengajuan[session['nik']] = {'desc': desc, 'status': 'menunggu persetujuan'}
            json.dump(app_data, open('data.json', 'w'), indent=4)
            print('Pengajuan berhasil dibuat.')
        elif menu == 2:
            os.system('clear')
            if not pengajuan.get(session['nik']):
                print('Anda belum membuat pengajuan.')
                input('\nTekan enter untuk melanjutkan...\n')
                continue
            
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
                print('Sayang sekali, Anda dapat membuat ulang pengajuan dan\nkembali melewati prosedur birokasi sesuai protokol')
            
            if kena_banned:
                print('Status akun : TIDAK SEHAT / KENA BANNED')
                print('[!] Akun Anda terkena banned')
                print(f'Alasan pemblokiran: \n{blacklist[session['nik']]['desc']}')
            else:
                print('Status akun : SEHAT')
                
            input('\nTekan enter untuk melanjutkan...\n')
        elif menu == 3:
            exit()

        