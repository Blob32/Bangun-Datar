"""
Tugas Akhir Mata Kuliah Program Komputer

Idensitas ==========================
|Nama           : Dzia Ulhaq       |
|NIM            : 1232050176       |
|Kelas          : 3E/2024          |
====================================

Tugas Akhir ========================
|Mata Kuliah    : Program Komputer |
|Tugas          : Membuat Program  |
|                 Matematika       |
|Bahasa          : Python          |
|Dosen pengampu : Rikirik          |
|                 Nurdiansyah, M.Pd|
====================================
"""
# PROGRAM UTAMA (HOME PAGE)
#==============================

# Modul
import time # Module time, untuk mengatur jalannya program agar ada jeda
import math  # Module math, untuk menggunakan fungsi yang ada di module math
import os # Module os, untuk mengambil fungsi os, yang akan digunakan untuk membersihkan direktori awal

#Lokal modul
import hitung # Module hitung, berisi fungsi rumus bangun datar
import belajar # Module belajar, berisi fungsi penjelasan bangun datar
import play # Modul play, berisi latihan soal

#==============================

def clear_screen(): #untuk membersihan direktori awal
    if os.name == "nt":
        os.system("cls") #untuk windows
    else:
        os.system("clear") #untuk linux, mac
clear_screen()

#==============================
# Fungsi untuk menyajikan informasi dari program
def info():
    print("\nProgram Komputer\n")
    time.sleep(2)
    print(
        "Program Belajar Matematika Geometri Bangun Datar\n"
        "Deskripsi:\n"
        "Program ini dibuat untuk memenuhi tugas akhir dari mata kuliah Porgram Komputer, Pendidikan Matematika 2024.Program ini juga bertujuan untuk menjadi gambaran awal dari aplikasi pembelajaran Matematika Geometri Bangun Datar, dengan meneparkan gameplay seperti dungeon seperti game-game saat ini, menurut saya ini cukup menarik."
        '''
        \nBangun Datar Yang Telah di Sediakan:
        ======= Menu Bangun Datar =======
        [1] Segitiga △           
        [2] Persegi ☐            
        [3] Persegi Panjang ▭    
        [4] Trapesium ⏢          
        [5] Jajar Genjang ▱      
        [6] Lingkaran ⬤          
        =================================
        '''
    )
    input(f"\nTekan Enter untuk Malanjutkan...")
# Fungsi untuk menyajikan panduan penggunaan program
def panduan():
    print("\nPanduan Penggunaan Program")
    print("\n1. Tampilan Menu Utama: [main.py]")
    print('''
=================================================
Selamat Datang di Program Geometri Bangun Datar!!
=================================================
        = Belajar Matematika: Geometri =
        ====== Luas Bangun Datar =======
        ================================
        ============= MENU =============
        |   [?] Panduan Penggunaan     |
        |   [!] Informasi Program      |
        --------------------------------
        | [1] Belajar Bangun Datar     |
        | [2] Latihan Soal Bangun Datar|
        | [3] Kalkulator Bangun Datar  |
        | [0] Exit                     |
        ================================

Panduan Opsi Menu:
    - Ketik 1 untuk masuk ke mode Belajar Bangun Datar.
    - Ketik 2 untuk memulai Latihan Soal Bangun Datar.
    - Ketik 3 untuk menggunakan Kalkulator Bangun Datar.
    - Ketik ? untuk melihat panduan penggunaan program ini.
    - Ketik ! untuk melihat informasi tentang program dan pengembang.
    - Ketik 0 untuk keluar dari program.
    ''')
    time.sleep(10)
    print("\n2. Belajar Bangun Datar: [belajar.py]")
    print('''
    ================================
    = Belajar Matematika: Geometri =
    ====== Luas Bangun Datar =======
    
Mari Kita Baca dengan seksama penjelasan dari masing-masing bangun datar berikut.

    ======= Menu Bangun Datar =======
    |   [1] Segitiga △              |
    |   [2] Persegi ☐               |
    |   [3] Persegi Panjang ▭       |
    |   [4] Trapesium ⏢             |
    |   [5] Jajar Genjang ▱         |
    |   [6] Lingkaran ⬤             |
    |   [0] Kembali                 |
    =================================
Setelah memilih bangun datar anda akan disajikan dengan penjelasan bangun datar.
Penjelasan bangun datar berisi: 
    - pengertian sederhana
    - ciri-ciri
    - rumus luas\cara menghitung luas
    - dan contoh soal
    ''')
    time.sleep(10)
    print("\n3. Kalkulator Bangun Datar: [hitung.py]")
    print('''
    ================================
        Menu Yang di Sajikan
    ======= Menu Bangun Datar =======
    |   [1] Segitiga △              |
    |   [2] Persegi ☐               |
    |   [3] Persegi Panjang ▭       |
    |   [4] Trapesium ⏢             |
    |   [5] Jajar Genjang ▱         |
    |   [6] Lingkaran ⬤             |
    |   [7] Tampilkan Tabel Hasil   |
    |   [0] Kembali                 |
    =================================

    > Masukkan pilihan Anda (0-6):
    
Setelah anda memilih bangun datar maka, anda akan disajikan kalkulator perhitungan dari bangun datar tersebut.
setelah anda melakukan perhitungan, maka data setelah perhingan tersebut akan dimasukkan ke dalam sebuah tabel history.
    +-----------------+--------+
    | Bangun Datar    | Luas   |
    +-----------------+--------+
    | Segitiga        | 15.0   |
    | Persegi         | 25.0   |
    | ...             | ...    |
    +-----------------+--------+
    ''')
    time.sleep(10)
    print("4. Latihan Soal Bangun Datar: [play.py]\n")
    print("Untuk Penjelasan ini akan diberikan pada saat Anda Masuk ke Latihan Soal")
    input(f"\nTekan Enter untuk Malanjutkan...")
# Fungsi utama yang menjalankan program
def main():
    #============================== Perulangan
    while True:
        print("Selamat Datang di Program Geometri Bangun Datar!!")
        print('''
        = Belajar Matematika: Geometri =
        ====== Luas Bangun Datar =======\n
        ============= MENU =============
        |   [?] Panduan Pengunaan      |
        |   [!] Infromasi Program      |
        --------------------------------
        | [1] Belajar Bangun Datar     |
        | [2] Latihan Soal Bangun Datar|
        | [3] Kalkulator Bangun Datar  |
        | [0] Exit                     |
        ================================
        ''')

        menu = {
            '?': panduan,
            '!': info,
            '1': belajar.main,
            '2': play.main,
            '3': hitung.main
        }
        #==============================
        #============================== User Input
        pilih = input("Masukkan pilihan Anda (0-3 / ?/ !): ")
        #============================== Pengkondisian berdasarkan inputan user
        if pilih in menu:
            menu[pilih]()
        elif pilih == '0':
            #============================== User memilih untuk keluar dan akan dibawa kembali ke menu utama
            print("Terima Kasih Telah Menggunakan Program Geometri Bangun Datar!!")
            break
        else:
            print("Pilihan tidak ada. Silakan coba lagi!")

#============================== Untuk menjalankan fungsi (main)/menjalankan program utama
if __name__ == "__main__":
    main()