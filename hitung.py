# PROGRAM Pendukung
#==============================

# Module
import math #imporrt math: untuk menggunakan fungsi yang ada di module math
import time # Module time, untuk mengatur jalannya program agar ada jeda
import os # Module os, untuk mengambil fungsi os, yang akan digunakan untuk membersihkan direktori awal

#==============================
# Fungsi untuk memvalidasi nilai yang dimasukkan oleh user seperti: alas, sisi, tinggi, dan komponen lain untuk mencari luas
def get_num(prompt):
    #============================== Perulangan
    while True:
        try:
            value = float(input(prompt))
            #jika_input_angka_negatif
            if value < 0:
                print("Maaf, sebuah ukuran tidak mungkin negatif,  silakan ulangi lagi.")
            #jika_input_angka_Nol
            elif value == 0:
                print('Ukuran tidak berinilai 0, silahkan ulangi')
            else:
                return value
        #jika_inputan_bukan_angka
        except ValueError:
            print("Maaf, yang Anda masukkan bukan angka bilangan bulat/desimal. Silakan ulangi lagi.")
#==============================

# Fungsi perhitungan luas bangun datar
# Fungsi Berisi: Variabel sebagai komponen perhitungan, dan Variabel luas yang berfungsi menghitung hasil luas dari bangun datar
def luasSegitiga():
    print("\n=== Segitiga ===\n")
    print("Mari Berhitung!")
    alas = get_num("Masukkan alas segitiga: ")
    tinggi = get_num("Masukkan tinggi segitiga: ")
    luasSegitiga = 0.5 * alas * tinggi
    print(f"Jadi Luas Segitiga dengan panjang alas {alas} cm, dan tinggi {tinggi} cm, adalah {luasSegitiga:.2f} cm^2")
    return luasSegitiga

def luasPersegi():
    print("\n=== Persegi ===\n")
    print("Mari Berhitung!")
    sisi = get_num("Masukkan panjang sisi persegi: ")
    luasPersegi = math.pow(sisi, 2) # sisi * sisi
    print(f"Jadi Luas Persegi dengan panjang sisi {sisi} cm, adalah {luasPersegi:.2f} cm^2")
    return luasPersegi

def luasPersegiPanjang():
    print("\n=== Persegi Panjang ===\n")
    print("Mari Berhitung!")
    panjang = get_num("Masukkan panjang persegi panjang: ")
    lebar = get_num("Masukkan lebar persegi panjang: ")
    luasPersegiPanjang = panjang * lebar
    print(f"Jadi Luas Persegi Panjang dengan panjang {panjang} cm, dan lebar {lebar} cm, adalah {luasPersegiPanjang:.2f} cm^2")
    return luasPersegiPanjang

def luasTrapesium():
    print("\n=== Trapesium ===\n")
    print("Mari Berhitung!")
    sisi_atas = get_num("Masukkan panjang sisi atas trapesium: ")
    sisi_bawah = get_num("Masukkan panjang sisi bawah trapesium: ")
    tinggi = get_num("Masukkan tinggi trapesium: ")
    luasTrapesium = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    print(f"Jadi Luas Trapesium dengan panjang sisi atas {sisi_atas} cm, sisi bawah {sisi_bawah} cm, dan tinggi {tinggi} cm, adalah {luasTrapesium:.2f} cm^2")
    return luasTrapesium

def luasJajarGenjang():
    print("\n=== Jajar Genjang ===\n")
    print("Mari Berhitung!")
    alas = get_num("Masukkan alas jajar genjang: ")
    tinggi = get_num("Masukkan tinggi jajar genjang: ")
    luasJajarGenjang = alas * tinggi
    print(f"Jadi Luas Jajar Genjang dengan panjang alas {alas} cm, dan tinggi {tinggi} cm, adalah {luasJajarGenjang:.2f} cm^2")
    return luasJajarGenjang

def luasLingkaran():
    print("\n=== Lingkaran ===\n")
    print("Mari Berhitung!")
    radius = get_num("Masukkan radius lingkaran: ")
    luasLingkaran = float(f"{math.pi:.2f}" ) * math.pow(radius,2)
    print(f"Jadi Luas Lingkaran dengan radius {radius} cm dengan pi(π) 3.14, adalah {luasLingkaran} cm^2")
    return luasLingkaran

def history(data):
    print("History: Tabel Hasil Perhitungan\n")
    print("\n+-----------------+-------------+")
    print("| Bangun Datar    | Luas (cm^2) |")
    print("+-----------------+-------------+")
    for item in data:
        print(f"| {item[0]:<15} | {item[1]:<11.2f} |")
    print("+-----------------+-------------+")
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
    data = [] #menampilkan data luas yang telah dilakukan
    #============================== Perulangan
    while True:
        #============================== Menu Bangun Datar 
        print('''
        = Belajar Matematika: Geometri =
        = Menghitung Luas Bangun Datar =\n
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
        ''')
        #==============================
        #============================== User Input
        pilihan = input("Masukkan pilihan Anda (0-7): ")

        #============================== Pengkondisian berdasarkan inputan user
        if pilihan == "1":
            #============================== Menjalankan fungsi bangun datar
            #============================== variabel 'hasil': untuk menyimpan nilai dari luas bangun datar
            hasil = luasSegitiga()
            time.sleep(2)
            #============================== Menyimpan data hasil perhitungan luas
            data.append(["Segitiga", hasil])
            #============================== 
        elif pilihan == "2":
            #============================== Menjalankan fungsi bangun datar
            #============================== variabel 'hasil': untuk menyimpan nilai dari luas bangun datar
            hasil = luasPersegi()
            time.sleep(2)
            #============================== Menyimpan data hasil perhitungan luas
            data.append(["Persegi", hasil])
            #============================== 
        elif pilihan == "3":
            #============================== Menjalankan fungsi bangun datar
            #============================== variabel 'hasil': untuk menyimpan nilai dari luas bangun datar
            hasil = luasPersegiPanjang()
            time.sleep(2)
            #============================== Menyimpan data hasil perhitungan luas
            data.append(["Persegi Panjang", hasil])
            #============================== 
        elif pilihan == "4":
            #============================== Menjalankan fungsi bangun datar
            #============================== variabel 'hasil': untuk menyimpan nilai dari luas bangun datar
            hasil = luasTrapesium()
            time.sleep(2)
            #============================== Menyimpan data hasil perhitungan luas
            data.append(["Trapesium", hasil])
            #============================== 
        elif pilihan == "5":
            #============================== Menjalankan fungsi bangun datar
            #============================== variabel 'hasil': untuk menyimpan nilai dari luas bangun datar
            hasil = luasJajarGenjang()
            time.sleep(2)
            #============================== Menyimpan data hasil perhitungan luas
            data.append(["Jajar Genjang", hasil])
            #============================== 
        elif pilihan == "6":
            #============================== Menjalankan fungsi bangun datar
            #============================== variabel 'hasil': untuk menyimpan nilai dari luas bangun datar
            hasil = luasLingkaran()
            time.sleep(2)
            #============================== Menyimpan data hasil perhitungan luas
            data.append(["Lingkaran", hasil])
            #============================== 
        elif pilihan == "7":
            #============================== Melihat data yang telah terkumpul
            if data:
                history(data)
                time.sleep(2)
            else:
            #============================== Jika data belum ada yang masuk
                print("Belum ada data yang dimasukkan!")
                time.sleep(2)
        elif pilihan == "0":
            #============================== User memilih untuk keluar dan akan dibawa kembali ke menu utama
            print("Keluar, Tunggu sebentar...")
            time.sleep(3)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("Input harus berupa (0-7 / ?/ !)")
            time.sleep(1)

#============================== Untuk menjalankan fungsi (main)/menjalankan program
# if __name__ == "__main__":
#     main()