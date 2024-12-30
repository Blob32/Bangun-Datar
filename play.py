# PROGRAM Pendukung [Latihan Soal]
#==============================

# Module
import time # Module time, untuk mengatur jalannya program agar ada jeda
import math  # Module math, untuk menggunakan fungsi yang ada di module math
import random # Module random, digunakan untuk mendapatkan nilai untuk komponen bangun datar agar setiap komponen tidak memiliki nilai yang sama
import os # Module os, untuk mengambil fungsi os, yang akan digunakan untuk membersihkan direktori awal

#Warna
merah = "\033[91m"
hijau = "\033[92m"
kuning = "\033[93m"
biru = "\033[94m"
ungu = "\033[95m"
cyan = "\033[96m"
reset = "\033[0m"
#==============================

# Fungsi untuk memvalidasi nilai yang dimasukkan oleh user
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

def clear_screen(): #untuk membersihan direktori awal
    if os.name == "nt":
        os.system("cls") #untuk windows
    else:
        os.system("clear") #untuk linux, mac
clear_screen()

#==============================

def hitung_exp(level, is_boss=False):
    base_exp = {1: 10, 2: 20, 3: 50}  # EXP dasar untuk setiap level
    if is_boss:
        multiplier = random.uniform(2, 4)  # Multiplier acak untuk soal boss (2-4 kali EXP)
        return int(base_exp[level] * multiplier)
    return base_exp[level]

#==============================

def teks_load(teks, delay=0.05):
    for huruf in teks:
        print(huruf, end="", flush=True)
        time.sleep(delay)
    print()

#==============================

# Fungsi untuk Intro
def dungeon_intro():
    import main
    clear_screen()
    #==============================
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("        🏰 Selamat Datang Player 🏰         ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    #==============================
    time.sleep(3)
    print("Siapkah Anda menghadapi tantangan besar dan menjadi seorang legenda?")
    print(f"> Tekan {ungu}[y]{reset} untuk Masuk ke Arena")
    print(f"> Tekan {ungu}[n]{reset} untuk Kembali ke Menu Utama")
    #============================== User Input
    masuk = input(": ")
    #============================== Pengkondisian berdasarkan inputan user
    if masuk == "y":
        clear_screen()
        print("🔄 Menyiapkan Arena...")
        time.sleep(1)
        print("⏳ Mohon tunggu sebentar...")
        time.sleep(0.5)
        time.sleep(3)
        masuk_arena() # Player Masuk Ke Arena

    elif masuk == "n":
        main.main() # Player Kembali ke Menu Utama [main.py]

    else:
        print("Maaf, input yang kamu masukkan tidak valid. Silakan coba lagi.")
        time.sleep(2)
        dungeon_intro()
#==============================

# Fungsi untuk Masuk Arena
def masuk_arena():
    clear_screen()
    #==============================
    print("⚔️  Anda Memasuki Arena ⚔️\n")
    time.sleep(3)
    global nama_player
    nama_player = input(f"Masukkan Nama Anda, Player: {hijau}")
    #==============================
    time.sleep(3)
    clear_screen()
    #==============================
    print(f"{reset}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"       ✨ Selamat Datang, {hijau}{nama_player}{reset}! ✨  ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    #==============================
    time.sleep(3)

    #============================== Status Awal
    print("🌟 Status Anda:")
    print(f" - 💖 HP: 〚{hijau}████████████████████{reset}〛{hijau}100%{reset}")
    print(f" - 🔥 EXP: 0 ")
    time.sleep(2)
    #==============================
    input(f"\n{hijau}Tekan Enter untuk memulai petualangan Anda...{reset}")
    #==============================
    time.sleep(2)
    pass
#==============================

# Fungsi untuk Aturan Gameplay
def gameplay():
    clear_screen()
    #==============================
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("           ⚔️  Panduan Permainan ⚔️          ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")    
    #==============================
    time.sleep(2)
    #============================== Tujuan Permainan
    print("🌟 Tujuan Permainan:  ")
    print(" - Kalahkan musuh dengan menjawab soal matematika.  ")
    print(" - Setiap jawaban benar memberikan EXP untuk meningkatkan gelar Anda!  ")
    print(" - Gelar Tertinggi: Master of Dungeon!\n")
    #==============================
    time.sleep(2)
    #============================== Level yang tersedia
    print("🛡️  Level:")
    print(f" 1️⃣  Level {hijau}Warrior.{reset}")
    print(f" 2️⃣  Level {merah}Average.{reset}")
    print(f" 3️⃣  Level {ungu}Legend.{reset}\n")
    #==============================
    time.sleep(2)
    #============================== Peratuan Permainan
    print("🧩 Peraturan Permainan:")
    print(" - Jawaban salah akan mengurangi HP Anda!")
    print(" - Kalahkan semua minion sebelum menghadapi Boss di akhir setiap dungeon.")
    print(" - Jangan biarkan HP Anda mencapai 0, atau permainan selesai!")
    print(" - EXP hanya bisa didapatkan dengan mengalahkan musuh melalui perhitungan soal yang tepat\n")
    #==============================
    time.sleep(2)
    #==============================
    print(f"🔥 Persiapkan dirimu, {hijau}{nama_player}{reset}!\n")
    time.sleep(2)
    #============================== Menampilkan Peta Arena
    print("🗺️  Peta")
    #==============================
    print(f'''
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
    |  『Arena』📍Posisi {hijau}Player{reset}                              |
    |                                                        |
    |       ━━━━━━━━━{ungu}Level 1{reset}━━━━━━━━━━━━━━━━━━━━━━━━━━━      |
    |       D       ┵                 |               |      |
    |       U       ┲                 |     {merah}"BOSS"{reset}    |      |
    |       N       |                 ┵     {merah}"BASE"{reset}    |      |
    |       G       |                 ┲               |      |
    |       E       |{ungu}Level 2{reset}━━━━━━━━━━━━━━━━━━━━━━|━|━━      |
    |       O       |                   |             |      |
    |       N       |      {merah}"BOSS"{reset}       |             |      |
    |       ┵       |      {merah}"BASE"{reset}       ┵             |      |
    |               |                   ┲             |      |
    |       ┲       |{ungu}Level 3{reset}━━|━  ━|━━━━━━━━━━━━━━━━━━━      |
    |       |       |               |                 |      |
    |       |       |               |                 |      |
    |       |       |               ┵                 |      |
    |       |       |                   {merah}"BOSS BASE"{reset}   |      |
    |       |       |               ┲                 |      |
    |       |       |               |                 |      |
    |       |       |               |                 |      |
    |       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|━━ ━━|━━━━      |
    |                                                        |
    |                                                        |
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
    ''')
    #==============================
    time.sleep(2)
    input(f"\n{hijau}Tekan Enter untuk memasuki Dungeon...{reset}")
    time.sleep(2)
    #==============================

# Fungsi utama yang menjalankan program
def main():
    #============================== Level
    levels = {
        1: "Warrior",
        2: "Average",
        3: "Legend"
    }
    #============================== Variabel Statistik Pemain
    global player_hp, exp_level, benar_level, salah_level
    player_hp = 100  
    exp_level = 0
    benar_level = 0
    salah_level = 0
    #============================== Menjalankan fungsi awal, mulai dari intro dan gameplay
    dungeon_intro()
    gameplay()
    #==============================
    clear_screen()
    teks_load("[Dungeon Telah Terbuka!]", 0.1)
    teks_load("Memasuki Dungeon... Bersiap untuk bertarung!\n", 0.1)
    print("🔄 Menyiapkan Dungeon...")
    time.sleep(1)
    print("⏳ Mohon tunggu sebentar...")
    time.sleep(0.5)
    print("⚙️  Mempersiapkan lawan...")
    time.sleep(3)
    clear_screen()
    #============================== Item Achievement
    achievements = ("Novice Explorer", "Challenger", "The Conqueror", "Master of Dungeon")
    #==============================
    
    # Memulai Permainan
    for level in range(1, 4):
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"  🔥 Level {level}: {levels[level]} 🔥")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        time.sleep(3)
        
        teks_load("Anda memasuki ruangan gelap dan mendengar langkah kaki...  ", 0.1)
        print("⚔️  Minion muncul! Bersiaplah untuk bertarung! ⚔️")
        #==============================
        print("Kalahkan Para Kroco tersebut!🔥")
        time.sleep(1)

        #============================== Soal untuk Minion
        for i in ( "Assasin", "Tanker", "Fighter", "Archer", "Mage"):
            print(f"\n♦️ Minion Tipe {ungu}{i}{reset} Sedang Menujumu!")
            time.sleep(0.5)
            print("Serang!! ⚔️")
            time.sleep(2)
            #============================== Pemilihan soal untuk masing-masing minion secara acak
            bangun_datar = random.choice(["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran", "Trapesium", "Jajar Genjang", "Sulit"])

            #============================== Pengkondisian sesuai dengan pilihan[random.choice()]
            #============================== Soal untuk Persegi
            if bangun_datar == "Persegi":
                sisi = random.randint(1, 10 * level)
                jawaban = sisi ** 2
                user_input = float(input(f"\n🧩 Soal: \nHitung luas persegi dengan sisi {sisi} cm: "))
            
            #============================== Soal untuk Persegi Panjang
            elif bangun_datar == "Persegi Panjang":
                panjang = random.randint(1, 10 * level)
                lebar = random.randint(1, 10 * level)
                jawaban = panjang * lebar
                user_input = get_num(f"\n🧩 Soal: \nHitung luas persegi panjang dengan panjang {panjang} cm dan lebar {lebar} cm: ")
            
            #============================== Soal untuk Segitiga
            elif bangun_datar == "Segitiga":
                alas = random.randint(1, 10 * level)
                tinggi = random.randint(1, 10 * level)
                jawaban = 0.5 * alas * tinggi
                user_input = get_num(f"\n🧩 Soal: \nHitung luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm: ")
            
            #============================== Soal untuk Lingkaran
            elif bangun_datar == "Lingkaran":
                radius = random.randint(1, 10 * level)
                jawaban = float(f"{math.pi:.2f}" ) * math.pow(radius,2)
                user_input = get_num(f"\n🧩 Soal: \nHitung luas lingkaran dengan jari-jari {radius} cm: ")

            #============================== Soal untuk Trapesium
            elif bangun_datar == "Trapesium":
                sisi_atas = random.randint(1, 10 * level)
                sisi_bawah = random.randint(1, 10 * level)
                tinggi = random.randint(1, 10 * level)
                jawaban = 0.5 * (sisi_atas + sisi_bawah) * tinggi
                user_input = get_num(f"\n🧩 Soal: \nHitung luas trapesium dengan sisi sejajar {sisi_atas} cm, {sisi_bawah} cm, dan tinggi {tinggi} cm: ")

            #============================== Soal untuk Jajar Genjang
            elif bangun_datar == "Jajar Genjang":
                alas = random.randint(1, 10 * level)
                tinggi = random.randint(1, 10 * level)
                jawaban = alas * tinggi
                user_input = get_num(f"\n🧩 Soal: \nHitung luas Jajar Genjang dengan alas {alas} cm, dan tinggi {tinggi} cm: ")

            #============================== Soal untuk pilihan tipe Sulit, luas gabungan bangun datar dua lingkaran
            elif bangun_datar == "Sulit":
                print(f"\n{merah}🔥  Minion memliki level yang lebih tinggi 🔥{reset}")
                print("Jaga-jaga!\n")
                radius_1 = random.randint(1, 10)
                radius_2 = random.randint(10, 15 * level)
                jawaban = (float(f"{math.pi:.2f}" ) * math.pow(radius_2,2))- (float(f"{math.pi:.2f}" ) * math.pow(radius_1,2))
                user_input = get_num(f"🧩 Soal: \nTerdapat sebuah lingkaran dengan jari-jari {radius_2} cm, dan di dalamnya terdapat lingkaran dengan jari-jari {radius_1} cm berada di tengahnya, hitunglah luas daerah yang tidak tertutupi lingkaran yang lebih kecil: ")
            #==============================
            
            #============================== Evaluasi\Kalkulasi Jawaban
            damage = random.randrange(0, 11, 2) * level #Damage jika menjawab salah
            if math.isclose(user_input, jawaban, rel_tol = 0.01):
                #============================== Player Menang[Benar menjawab Soal]
                #============================== Variabel
                exp_soal = hitung_exp(level)
                exp_level += hitung_exp(level)
                benar_level += 1
                #==============================
                print(f"✔️ {hijau}Jawaban benar{reset}!")
                time.sleep(0.5)
                print(f"⚔️  Minion telah dikalahkan!")
                time.sleep(0.5)
                #==============================
                print(f"🌟 Anda mendapatkan {hijau}+{exp_soal} EXP!{reset}\n")
                time.sleep(0.5)
                #==============================
            else:
                #============================== Player Kalah[Salah menjawab Soal]
                #============================== Variabel
                player_hp -= damage
                salah_level += 1
                hp = f"{hijau}█"
                cap = int(player_hp/5)
                gap = f"{merah}█"
                hp_bar = (hp * cap) + (gap * (20 - cap))
                #==============================
                print(f"❌ {merah}Jawaban salah!{reset}")
                time.sleep(0.5)
                print(f"💔 Kamu terkena damage sebesar {merah}{damage} HP{reset}.")
                time.sleep(0.5)
                print(f"🩸 HP:〚{hp_bar}{reset}〛{player_hp}%")
                time.sleep(0.5)
                print(f"🌟 Jawaban yang benar adalah {jawaban:.2f}\n")
                time.sleep(2)
                #==============================
            # Cek jika HP habis
            if player_hp <= 0:
                #============================== HP player Habis
                cap = 0
                hp_bar = (hp * cap) + (gap * (20 - cap))
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"🩸 HP:〚{hp_bar}{reset}〛{player_hp}%")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                #==============================
                print("\n💀 HP Anda habis! Game Over💀.")
                #============================== Statistik Pemain
                time.sleep(0.5)
                print(f"🔥 Total EXP: {exp_level}")
                time.sleep(0.5)
                print(f"✔️ Total soal benar: {benar_level}")
                time.sleep(0.5)
                print(f"❌ Total soal salah: {salah_level}")
                time.sleep(0.5)
                #==============================
                return
                #==============================                
            #==============================
        # BOSS BASE
        if level == 1:
            #============================== Soal BOSS Level 3: Monark of Dragon
            #============================== Variabel
            panjang = random.randint(10, 25 * level)
            lebar = random.randint(10, 20 * level)
            radius = random.randint(1, 5 * level)
            #============================== Variabel Jawaban
            jawaban = (panjang * lebar) - (float(f"{math.pi:.2f}" ) * math.pow(radius,2))
            #============================== Intro BOSS
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"🏰 {merah}Anda telah mencapai Boss Base!{reset}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            time.sleep(0.5)
            print("Anda telah melewati rintangan untuk datang ke sini! Saatnya menghadapi Boss Level Ini.")
            teks_load("Memasuki Ruang Boss...", 0.1)
            time.sleep(0.5)
            print("\n🔥 Suara gemuruh memenuhi ruangan! Anda merasakan hawa panas yang semakin dekat.")
            teks_load("Sosok besar perlahan muncul dari kegelapan...", 0.1)
            time.sleep(1)
            #==============================
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            teks_load(f"{kuning}[Boss Warrior]: HIGH ORC 🪓{reset}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            #==============================
            time.sleep(0.5)
            print(f"💬 {kuning}HIGH ORC{reset}: \"Siapa yang berani mengganggu kedamaian tempatku?! Bersiaplah untuk pertarunganmu!\"")
            time.sleep(0.5)
            print(f"💬 {hijau}Kamu{reset}: \"Aku tidak takut! Aku akan mengalahkanmu!!\"")
            #==============================
            time.sleep(0.5)
            input(f"\n{hijau}Tekan Enter untuk Bersiap Menyerang...{reset}")
            time.sleep(0.5)
            #==============================
            user_input = get_num(f"🧩 Soal: \n\"Sebuah taman berbentuk persegi panjang memiliki panjang {panjang} m dan lebar {lebar} m. Di tengahnya terdapat kolam berbentuk lingkaran dengan jari-jari {radius} m. Berapa luas taman yang tidak tertutupi kolam? (π = 3.14)\"\n: ")
            #==============================
        elif level == 2:
            #============================== Soal BOSS Level 2: Dark Knight
            #============================== Variabel
            sisi_atas = random.randint(1, 10 * level)
            sisi_bawah = random.randint(1, 10 * level)
            tinggi = random.randint(1, 10 * level)
            panjang = sisi_bawah
            lebar = random.randint(1, 10)
            #============================== Variabel Jawaban
            jawaban = (0.5 * (sisi_atas + sisi_bawah) * tinggi) + (panjang * lebar)
            #============================== Intro BOSS
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"🏰 {merah}Anda telah mencapai Boss Base!{reset}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            print("Anda telah melewati semua tantangan di level sebelumnya. Kini, perjalanan Anda membawa Anda ke lawan yang jauh lebih berbahaya.")
            teks_load("Melangkah ke Ruang Boss...", 0.1)
            time.sleep(0.5)
            print("\n🌒 Suasana menjadi mencekam. Anda mendengar suara langkah berat yang mendekat.")
            teks_load("Bayangan besar dengan aura kegelapan muncul dari kegelapan...", 0.1)
            time.sleep(1)
            #==============================
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            teks_load(f"{ungu}[Boss Average]: DARK KNIGHT ⚔️{reset}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            #==============================
            time.sleep(0.5)
            print(f"💬 {ungu}DARK KNIGHT{reset}: \"Kegelapan adalah kekuatan yang tak dapat kau lawan. Bersiaplah untuk musnah!\"")
            time.sleep(0.5)
            print(f"💬 {hijau}Kamu{reset}: \"HAH! Kaulah Yang Harusnya Bersiap!!\"")
            #==============================
            time.sleep(0.5)
            input(f"\n{hijau}Tekan Enter untuk Bersiap Menyerang...{reset}")
            time.sleep(0.5)
            #============================== Soal
            user_input = get_num(f"🧩 Soal: \n\"Sebuah kebun berbentuk gabungan bangun datar dari trapesium dan persegi panjang. Trapesium memiliki panjang sisi sejajar {sisi_atas} m dan {sisi_bawah} m, serta tinggi {tinggi} m. Dan persegi panjang memiliki panjang {panjang} m dan lebar {lebar} m. Berapa luas kebun yang tersebut?\"\n: ")
            #==============================
        elif level == 3:
            #============================== Soal BOSS Level 3: Monark of Dragon
            #============================== Variabel
            sisi_segitiga = random.randint(20, 35)
            radius = 0.5 * sisi_segitiga
            sisi_persegi = random.randint(10, 17)
            #==============================
            luas_segitiga = (math.sqrt(3) / 4) * math.pow(sisi_segitiga, 2)
            luas_lingkaran = float(f"{math.pi:.2f}" ) * math.pow(radius,2)
            luas_persegi = math.pow(sisi_persegi, 2)
            #============================== Variabel Jawaban
            jawaban = luas_segitiga + luas_lingkaran - luas_persegi
            #============================== Intro BOSS
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"🏰 {merah}Anda telah mencapai Boss Base!{reset}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            print("Ini adalah ujian terakhir. Anda telah berhasil melewati rintangan yang tak terhitung, tetapi lawan terbesar Anda kini menanti.")
            teks_load("Memasuki Sarang Naga...", 0.1)
            time.sleep(2)
            print("\n🔥🔥 Suhu ruangan meningkat drastis! Anda melihat percikan api dan asap di udara.")
            teks_load("Gema raungan besar memenuhi arena, membuat tanah bergetar...", 0.1)
            time.sleep(1)
            #==============================
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            teks_load(f"{merah}[Boss Legend]: MONARK OF DRAGON 🐉{reset}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            #==============================
            time.sleep(0.5)
            print(f"💬 {merah}MONARK OF DRAGON{reset}: \"Kau hanyalah debu di hadapan kekuatan naga yang agung. Bersiaplah untuk akhir yang tak terelakkan!\"")
            time.sleep(0.5)
            print(f"💬 {hijau}Kamu{reset}: \"Kita Lihat Saja!!\"")
            #==============================
            time.sleep(0.5)
            input(f"\n{hijau}Tekan Enter untuk Bersiap Menyerang...{reset}")
            time.sleep(0.5)
            #============================== Soal
            print(
            f"🧩 Soal: \nSebuah lapangan baseball berbentuk seperti berlian (gabungan dari segitiga sama kaki dan setengah lingkaran) dengan komponen sebagai berikut:\n"
            f"- Bagian atas lapangan berbentuk segitiga sama sisi dengan panjang sisi {sisi_segitiga} meter.\n"
            f"- Bagian bawah lapangan berbentuk setengah lingkaran dengan jari-jari sebesar {radius} meter.\n"
            f"- Di tengah lapangan terdapat sebuah persegi berukuran {sisi_persegi} meter × {sisi_persegi} meter yang merupakan area permainan dalam.\n"
            )
            time.sleep(2)
            print("💡  Hit: Luas Segitiga sama sisi = (√3 / 4) × sisi^2")
            #==============================
            user_input = get_num(f"Tentukan Luas lapangan yang bukan arena permainan dalam: ")
            #==============================
        #==============================

        #============================== Evaluasi\Kalkulasi Jawaban
        damage = random.randrange(10, 21, 2)  #Damage jika menjawab salah
        if math.isclose(user_input, jawaban, rel_tol = 0.01):
            #============================== Player Menang[Benar menjawab Soal]
            #============================== Variabel
            boss_exp = hitung_exp(level, is_boss = True)
            exp_level += boss_exp
            benar_level += 1
            #==============================
            teks_load("\nKau Cukup Hebat, Tapi Sayang Aku Lebih Hebat... Aku Tidak Akan Melupakanmu...", 0.1)
            time.sleep(3)
            print(f"✔️  {hijau}Jawaban benar{reset}!")
            time.sleep(0.5)
            print(f"⚔️  BOSS telah Dikalahkan!")
            time.sleep(0.5)
            #==============================
            print(f"🌟  Anda mendapatkan {hijau}+{boss_exp} EXP!{reset}\n")
            time.sleep(5)
            #==============================
        else:
            #============================== Player Kalah[Salah menjawab Soal]
            #============================== Variabel
            player_hp -= damage
            salah_level += 1
            hp = f"{hijau}█"
            cap = int(player_hp/5)
            gap = f"{merah}█"
            hp_bar = (hp * cap) + (gap * (20 - cap))
            #==============================
            teks_load("\nAku Terlalu Cepat untuk Datang Kemari...", 0.1)
            time.sleep(3)
            print(f"❌ {merah}Jawaban salah!{reset}")
            time.sleep(0.5)
            print(f"{merah}BOSS Terlalu Kuat!{reset}\n")
            time.sleep(0.5)
            #==============================
            print(f"💔 Kamu terkena damage sebesar {merah}{damage} HP{reset}.")
            time.sleep(0.5)
            print(f"🩸 HP:〚{hp_bar}{reset}〛{player_hp}%")
            time.sleep(0.5)
            print(f"🌟 Jawaban yang benar adalah {jawaban:.2f}\n")
            time.sleep(5)
            #==============================
        if player_hp <= 0:
            #============================== HP player Habis
            cap = 0
            hp_bar = (hp * cap) + (gap * (20 - cap))
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"🩸 HP:〚{hp_bar}{reset}〛{player_hp}%")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            #==============================
            print("\n💀 HP Anda habis! Game Over💀.\n")
            #============================== Statistik Pemain
            time.sleep(0.5)
            print(f"🔥 Total EXP: {exp_level}")
            time.sleep(0.5)
            print(f"✔️ Total soal benar: {benar_level}")
            time.sleep(0.5)
            print(f"❌ Total soal salah: {salah_level}")
            time.sleep(3)
            #==============================
            return
            #==============================
        #==============================
        
    #============================== Variabel Statistik
    total_exp = exp_level
    soal_benar = benar_level
    soal_salah = salah_level

    #============================== Penutup
    clear_screen()
    print("🔄 Menyelesaikan Dungeon...")
    time.sleep(1)
    print("⏳ Mohon tunggu sebentar...")
    time.sleep(0.5)
    print("⚙️  Keluar Dari Dungeon...")
    time.sleep(3)
    clear_screen()
    print(f"🎉 Selamat {hijau}{nama_player}{reset} Kamu Telah Menyelesaikan Seluruh Dungeon\n")
    time.sleep(1)
    print("🔄 Menghitung Statistik Pemain...")
    time.sleep(1)
    print("⏳ Mohon tunggu sebentar...")
    time.sleep(3)
    clear_screen()
    #============================== Statistik Pemain
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 📊  Statistik Akhir Permainan")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    #==============================
    print(f"⚔️  Nama : {nama_player}")
    print(f"🩸  HP Terakhir:〚{hp_bar}{reset}〛{player_hp}%")
    print(f"🔥  Total EXP  : {total_exp}")
    print(f"✔️  Total soal benar: {soal_benar}")
    print(f"❌  Total soal salah: {soal_salah}\n")
    #==============================
    #============================== Pengkondisian untuk penentuan achievement yang didapatkan berdasarkan EXP pemain
    if total_exp >= 500:
        #============================== Jika EXP >= 500, Achievement: Master of Dungeon
        print(f"🎉 Selamat {hijau}{nama_player}{reset}")
        time.sleep(1)
        print(f"{biru} Anda telah Mendapatkan Achievement! {reset}")
        time.sleep(1)
        print(f"🎖️ Achievement: {merah}{achievements[3]}{reset}!")
        time.sleep(2)
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🔥  {ungu}HORMAT PADA SANG LEGENDA!, TUNDUKLAH PADA SANG RAJA!{reset} 👑 ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        #==============================
    elif total_exp >= 350:
        #============================== Jika EXP >= 350, Achievement: The Conqueror
        print(f"🎉 Selamat {hijau}{nama_player}{reset}")
        time.sleep(1)
        print(f"{biru}Anda telah Mendapatkan Achievement!{reset}")
        time.sleep(1)
        print(f"🎖️ Achievement: {merah}{achievements[2]}{reset}")
        time.sleep(2)
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"          🔥 {kuning} Kau Cukup Hebat Sebagai The Conqueror{reset}          ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        #==============================
    elif total_exp >= 250:
        #============================== Jika EXP >= 250, Achievement: Challenger
        print(f"🎉 Selamat {hijau}{nama_player}{reset}")
        time.sleep(1)
        print(f"{biru}Anda telah Mendapatkan Achievement!{reset}")
        time.sleep(1)
        print(f"🎖️ Achievement: {merah}{achievements[1]}{reset}")
        time.sleep(2)
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"             🔥 {hijau}Kau Cukup Terampil Juga Anak Muda{reset}            ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        #==============================
    elif total_exp >= 0:
        #============================== Jika EXP >= 0, Achievement: Novice Explorer", "
        print(f"🎉 Selamat {hijau}{nama_player}{reset}")
        time.sleep(1)
        print(f"{biru}anda telah Mendapatkan Achievement!{reset}")
        time.sleep(1)
        print(f"🎖️ Achievement: {merah}{achievements[0]}{reset}")
        time.sleep(2)
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" Teruslah berlatih untuk mencapai gelar MASTER OF LEGEND!💪  ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        #==============================
    #==============================
    
    #============================== Penutup
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("               🔥  Terima Kasih Telah Bermain!               ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    #==============================

    input(f"\n{hijau}Tekan Enter untuk Malanjutkan...{reset}")



#============================== Untuk menjalankan fungsi (main)/menjalankan program
# if __name__ == "__main__":
#     main()