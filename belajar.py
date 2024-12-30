# PROGRAM Pendukung
#==============================

# Module
import time # Module time, untuk mengatur jalannya program agar ada jeda
import math  # Module math, untuk menggunakan fungsi yang ada di module math
import random # Module random, digunakan untuk mendapatkan nilai untuk komponen bangun datar agar setiap komponen tidak memiliki nilai yang sama
import os # Module os, untuk mengambil fungsi os, yang akan digunakan untuk membersihkan direktori awal

#==============================
# Panjang sisi, alat, dan tinggi yang akan digunakan pada setiap contoh bangun datar
num = random.randint(1, 10)
num2 = random.randint(1, 15)
#==============================

# Fungsi penjelasan bangun datar
# Penjelasan sederhana berisi: pengertian, rumus luas, dan contohnya

def segitiga(): 
    print('''
    \n=== Segitiga ===
    Segitiga adalah bangun datar yang memiliki tiga sisi.
    Komponen Perhitungan: Alas dan Tinggi
    \nCiri-ciri:
    - Memiliki 3 sisi
    - Memiliki 3 sudut
    - Memiliki 3 titik sudut
    - Jumlah ketiga sudutnya selalu 180 derajat
    \nRumus Luas:
    Luas = 1/2 x Alas x Tinggi\n
    ''')
    #============================== Variabel untuk bangun datar sebagai contoh soal
    alas = num
    tinggi = num2
    luas = alas * tinggi * 0.5
    time.sleep(3)
    print("Contoh:")
    print(f"Ada sebuah segitiga dengan alas sebesar {alas} cm dan tinggi {tinggi}cm, maka luasnya dengan rumus tersebut adalah {luas:.2f} cm^2 \n")
    time.sleep(3)
#==============================

def persegi():
    print('''
    \n=== Persegi ===
    Persegi adalah bangun datar yang memiliki 4 sisi sama panjang.
    Komponen Perhitungan: Sisi
    \nCiri-ciri:
    - Memiliki 4 sisi yang sama panjang
    - Memiliki 4 sudut siku-siku (90 derajat)
    - Memiliki 4 sumbu simetri putar dan lipat
    - Memiliki 2 diagonal yang sama panjang dan berpotongan tegak lurus
    \nRumus Luas:
    Luas = Sisi x Sisi\n
    ''')
    #============================== Variabel untuk bangun datar
    sisi = num
    luas = math.pow(sisi, 2) # sisi * sisi
    time.sleep(3)
    print("Contoh:")
    print(f"Ada sebuah persegi dengan sisi sebesar {sisi} cm sehingga luasnya dengan rumus tersebut adalah {luas:.2f} cm^2 \n")
    time.sleep(3)
#==============================

def persegiPanjang():
    print('''
    \n=== Persegi Panjang ===
    Persegi panjang adalah bangun datar yang memiliki dua pasang sisi yang berhadapan sama panjang.
    Komponen Perhitungan: Panjang dan Lebar
    \nCiri-ciri:
    - Memiliki 2 pasang sisi yang berhadapan sama panjang dan sejajar
    - Memiliki 4 sudut siku-siku (90 derajat)
    - Memiliki 2 sumbu simetri putar dan lipat
    - Memiliki 2 diagonal yang sama panjang dan berpotongan di tengah
    \nRumus Luas:
    Luas = Panjang x Lebar\n
    ''')
    #============================== Variabel untuk bangun datar sebagai contoh soal
    panjang = num * 2
    lebar = num2 
    luas = panjang * lebar
    time.sleep(3)
    print("Contoh:")
    print(f"Ada sebuah persegi panjang dengan panjang sebesar {panjang} cm dan lebar {lebar}cm, maka luasnya dengan rumus tersebut adalah {luas:.2f} cm^2 \n")
    time.sleep(3)
#==============================

def trapesium():
    print('''
    \n=== Trapesium ===
    Trapesium adalah bangun datar yang memiliki sepasang sisi sejajar.
    Komponen Perhitungan: Sisi atas, Sisi bawah, dan Tinggi
    \nCiri-ciri:
    - Memiliki sepasang sisi sejajar
    - Memiliki 4 titik sudut
    - Bisa memiliki 1 sumbu simetri lipat (hanya untuk trapesium sama kaki)
    - Jenis-jenis trapesium: Trapesium siku-siku, trapesium sama kaki, trapesium sembarang
    \nRumus Luas:
    Luas = 1/2 x (Sisi atas + Sisi bawah) x Tinggi\n
    ''')
    #============================== Variabel untuk bangun datar sebagai contoh soal
    sisi_atas = num
    sisi_bawah = num + (num *0.5)
    tinggi = num2
    luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    time.sleep(3)
    print("Contoh:")
    print(f"Ada sebuah trapesium dengan panjang sisi atas sebesar {sisi_atas} cm, sisi bawah {sisi_bawah}cm, dan tinggi {tinggi} cm,  maka luasnya dengan rumus tersebut adalah {luas:.2f} cm^2 \n")
    time.sleep(3)
#==============================

def jajarGenjang():
    print('''
    \n=== Jajar Genjang ===
    Jajar genjang adalah bangun datar yang memiliki dua pasang sisi yang berhadapan sejajar dan sama panjang.
    Komponen Perhitungan: Alas dan Tinggi
    \nCiri-ciri:
    - Memiliki 2 pasang sisi yang berhadapan sama panjang dan sejajar
    - Memiliki 4 titik sudut, dua pasang sudut yang berhadapan sama besar
    - Sudut-sudut yang saling berdekatan jumlahnya 180 derajat
    - Tidak memiliki simetri lipat
    \nRumus Luas:
    Luas = Alas x Tinggi\n
    ''')
    #============================== Variabel untuk bangun datar sebagai contoh soal
    alas = num
    tinggi = num2
    luas = alas * tinggi
    time.sleep(3)
    print("Contoh:")
    print(f"Ada sebuah jajar genjang dengan alas sebesar {alas} cm dan tinggi {tinggi}cm, maka luasnya dengan rumus tersebut adalah {luas:.2f} cm^2 \n")
    time.sleep(3)
#==============================    

def lingkaran():
    print('''
    \n=== Lingkaran ===
    Lingkaran adalah bangun datar yang memiliki satu sisi lengkung yang disebut keliling.
    Komponen Perhitungan: Jari-jari
    \nCiri-ciri:
    - Memiliki jarak yang sama antara semua titik tepi ke pusat (jari-jari)
    - Memiliki simetri putar dan lipat yang tidak terhingga
    - Jumlah derajat lingkaran adalah 360 derajat
    - Tidak memiliki sisi atau sudut
    \nRumus Luas:
    Luas = π x (Jari-jari)^2
    dengan π = 3,14
    ''')
    #============================== Variabel untuk bangun datar sebagai contoh soal
    radius = num
    luas = float(f"{math.pi:.2f}" ) * math.pow(radius,2)
    time.sleep(3)
    print("Contoh:")
    print(f"Ada sebuah lingkaran dengan jari-jari sebesar {radius} dengan pi(π) 3.14, maka luasnya dengan rumus tersebut adalah {luas:.2f} cm^2 \n")
    time.sleep(3)
#==============================

#==============================

def clear_screen(): #untuk membersihan direktori awal
    if os.name == "nt":
        os.system("cls") #untuk windows
    else:
        os.system("clear") #untuk linux, mac
clear_screen()

#==============================

# Fungsi utama yang menjalankan program
def main():
    #============================== Perulangan
    while True:
        #============================== Menu Bangun Datar 
        print('''
        = Belajar Matematika: Geometri =
        ====== Luas Bangun Datar =======
        \nMari Kita Baca dengan seksama penjelasan dari masing-masing bangun datar berikut.\n
        ======= Menu Bangun Datar =======
        |   [1] Segitiga △              |
        |   [2] Persegi ☐               |
        |   [3] Persegi Panjang ▭       |
        |   [4] Trapesium ⏢             |
        |   [5] Jajar Genjang ▱         |
        |   [6] Lingkaran ⬤             |
        |   [0] Kembali                 |
        =================================
        ''')
        #==============================
        #============================== User Input
        pilihan = input("Masukkan pilihan Anda (0-6): ")

        #============================== Pengkondisian berdasarkan inputan user
        if pilihan == "1":
            #============================== Perulangan
            while True:    
                #============================== Menjalankan fungsi bangun datar
                segitiga()
                #============================== Input User: untuk mengulangi pembelajaran
                ulang = input("> Bagimana, apakah kamu sudah paham atau ingin mengulanginya lagi agar lebih paham? (ulang/lanjut): ").lower()
                if ulang == "ulang":
                    time.sleep(2)
                    print("\nTidak Mengapa, Mari kita belajar lagi!")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    continue
                elif ulang == "lanjut":
                    time.sleep(1)
                    print("\nWih Keren!!🔥")
                    print("Kamu sudah paham, mari kita lanjut ke materi selanjutnya")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi!")
        elif pilihan == "2":
            #============================== Perulangan
            while True:    
                #============================== Menjalankan fungsi bangun datar
                persegi()
                #============================== Input User: untuk mengulangi pembelajaran
                ulang = input("> Bagimana, apakah kamu sudah paham atau ingin mengulanginya lagi agar lebih paham? (ulang/lanjut): ").lower()
                if ulang == "ulang":
                    time.sleep(2)
                    print("\nTidak Mengapa, Mari kita belajar lagi!")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    continue
                elif ulang == "lanjut":
                    time.sleep(1)
                    print("\nWih Keren!!🔥")
                    print("Kamu sudah paham, mari kita lanjut ke materi selanjutnya")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi!")
        elif pilihan == "3":
            #============================== Perulangan
            while True:    
                #============================== Menjalankan fungsi bangun datar
                persegiPanjang()
                #============================== Input User: untuk mengulangi pembelajaran
                ulang = input("> Bagimana, apakah kamu sudah paham atau ingin mengulanginya lagi agar lebih paham? (ulang/lanjut): ").lower()
                if ulang == "ulang":
                    time.sleep(2)
                    print("\nTidak Mengapa, Mari kita belajar lagi!")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    continue
                elif ulang == "lanjut":
                    time.sleep(1)
                    print("\nWih Keren!!🔥")
                    print("Kamu sudah paham, mari kita lanjut ke materi selanjutnya")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi!")
        elif pilihan == "4":
            #============================== Perulangan
            while True:    
                #============================== Menjalankan fungsi bangun datar
                trapesium()
                #============================== Input User: untuk mengulangi pembelajaran
                ulang = input("> Bagimana, apakah kamu sudah paham atau ingin mengulanginya lagi agar lebih paham? (ulang/lanjut): ").lower()
                if ulang == "ulang":
                    time.sleep(2)
                    print("\nTidak Mengapa, Mari kita belajar lagi!")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    continue
                elif ulang == "lanjut":
                    time.sleep(1)
                    print("\nWih Keren!!🔥")
                    print("Kamu sudah paham, mari kita lanjut ke materi selanjutnya")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi!")
        elif pilihan == "5":
            #============================== Perulangan
            while True:    
                #============================== Menjalankan fungsi bangun datar
                jajarGenjang()
                #============================== Input User: untuk mengulangi pembelajaran
                ulang = input("> Bagimana, apakah kamu sudah paham atau ingin mengulanginya lagi agar lebih paham? (ulang/lanjut): ").lower()
                if ulang == "ulang":
                    time.sleep(2)
                    print("\nTidak Mengapa, Mari kita belajar lagi!")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    continue
                elif ulang == "lanjut":
                    time.sleep(1)
                    print("\nWih Keren!!🔥")
                    print("Kamu sudah paham, mari kita lanjut ke materi selanjutnya")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi!")
        elif pilihan == "6":
            #============================== Perulangan
            while True:    
                #============================== Menjalankan fungsi bangun datar
                lingkaran()
                #============================== Input User: untuk mengulangi pembelajaran
                ulang = input("> Bagimana, apakah kamu sudah paham atau ingin mengulanginya lagi agar lebih paham? (ulang/lanjut): ").lower()
                if ulang == "ulang":
                    time.sleep(2)
                    print("\nTidak Mengapa, Mari kita belajar lagi!")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    continue
                elif ulang == "lanjut":
                    time.sleep(1)
                    print("\nWih Keren!!🔥")
                    print("Kamu sudah paham, mari kita lanjut ke materi selanjutnya")
                    print("Tetap semangat💪")
                    time.sleep(4)
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi!")
        elif pilihan == "0":
            #============================== User memilih untuk keluar dan akan dibawa kembali ke menu utama
            print("Keluar, Tunggu sebentar...")
            time.sleep(3)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("Input harus berupa (0-6)")
            time.sleep(1)

#============================== Untuk menjalankan fungsi (main)/menjalankan program
# if __name__ == "__main__":
#     main()