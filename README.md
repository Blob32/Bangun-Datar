# Program Belajar Matematika Geometri Bangun Datar

Deskripsi:
Program ini dibuat untuk memenuhi tugas akhir dari mata kuliah Porgram Komputer, Pendidikan Matematika 2024.
Program ini juga bertujuan untuk menjadi gambaran awal dari aplikasi pembelajaran Matematika Geometri Bangun Datar, dengan meneparkan gameplay seperti dungeon seperti game-game saat ini, menurut saya ini cukup menarik.

Untuk penjelasan lebih lengkapnya ada di bawah ini:
```
**Menu Utama**
= Belajar Matematika: Geometri =
============= MENU =============
[?] Panduan Pengunaan    
[!] Infromasi Program    
--------------------------------
[1] Belajar Bangun Datar
[2] Latihan Soal Bangun Datar
[3] Kalkulator Bangun Datar
[0] Exit
================================

**Bangun Datar Yang Telah di Sediakan**
======= Menu Bangun Datar =======
[1] Segitiga △           
[2] Persegi ☐            
[3] Persegi Panjang ▭    
[4] Trapesium ⏢          
[5] Jajar Genjang ▱      
[6] Lingkaran ⬤          
=================================
```
## **Struktur file**

```
.
├── main.py        # Halaman utama
├── belajar.py     # Program Penjelasan materi bangun datar yaitu luas
├── hitung.py      # Program Operasi perhitungan luas bangun datar
├── play.py        # Program Latihan soal dengan penerapan gameplay dungeon
├── README.md      # Penjelasan tugas
└── __pycache__
    └── ...        # Module cache

```
=================================

**Module**
# Modul
    - import math  # Module math, untuk menggunakan fungsi yang ada di module math
    - import os # Module os, untuk mengambil fungsi os, yang akan digunakan untuk membersihkan direktori awal
    - import random # Module random, digunakan untuk mendapatkan nilai untuk komponen bangun datar agar setiap komponen tidak memiliki nilai yang sama

# Lokal modul, digunakan oleh main.py
    - import hitung # Module hitung, berisi fungsi rumus bangun datar
    - import belajar # Module belajar, berisi fungsi penjelasan bangun datar
    - import play # Modul play, berisi latihan soal
=================================

**Strutur Kode**

***A. Belajar Bangun Datar: belajar.py***
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

    > Masukkan pilihan Anda (0-6):
    
    = if pilihan 1-6:  maka akan menjalankan fungsi masing-masing bangun datar yang sesuai dengan menu yang ditampilkan
    ```
    Penjelasan bangun datar berisi:
    - pengertian sederhana
    - ciri-ciri
    - rumus luas\cara menghitung luas
    - dan contoh soal
    ```

    = elif pilihan 0: maka akan kembali ke menu utama di main.py

    > Bagimana, apakah kamu sudah paham atau ingin mengulanginya lagi agar lebih paham? (ulang/lanjut): 

    = if jawab ulang:
    Tidak Mengapa, Mari kita belajar lagi!
    Tetap semangat💪
    
    = elif jawab lanjut:
    Wih Keren!!🔥
    Kamu sudah paham, mari kita lanjut ke materi selanjutnya
    Tetap semangat💪

***B. Latihan Soal Bangun Datar: play.py***
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        🏰 Selamat Datang Player 🏰         
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Siapkah Anda menghadapi tantangan besar dan menjadi seorang legenda?
> Tekan [y] untuk Masuk ke Arena
> Tekan [n] untuk Kembali ke Menu Utama
= if: y
🔄 Menyiapkan Arena...
⏳ Mohon tunggu sebentar...
masuk_arena() # Player Masuk Ke Arena

= elif: n
main.main() # Player Kembali ke Menu Utama [main.py]

= else:
print("Maaf, input yang kamu masukkan tidak valid. Silakan coba lagi.")


masuk_arena()

    ⚔️  Anda Memasuki Arena ⚔️
    > Masukkan Nama Anda, Player:

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ✨ Selamat Datang, {nama_player}! ✨  
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    🌟 Status Anda
    - 💖 HP: 〚████████████████████〛100%
    - 🔥 EXP: 0

    > Tekan Enter untuk memulai petualangan Anda...

gameplay()
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            ⚔️  Panduan Permainan ⚔️         
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    🌟 Tujuan Permainan:  
    - Kalahkan musuh dengan menjawab soal matematika.  
    - Setiap jawaban benar memberikan EXP untuk meningkatkan gelar Anda!  
    - Gelar Tertinggi: Master of Dungeon!

    🛡️  Level:
    1️⃣  Level Warrior.
    2️⃣  Level Average.
    3️⃣  Level Legend.

    🧩 Peraturan Permainan:
    - Jawaban salah akan mengurangi HP Anda!
    - Kalahkan semua minion sebelum menghadapi Boss di akhir setiap dungeon.
    - Jangan biarkan HP Anda mencapai 0, atau permainan selesai!
    - EXP hanya bisa didapatkan dengan mengalahkan musuh melalui perhitungan soal yang tepat

    🔥 Persiapkan dirimu, {nama_player}

    🗺️  Peta
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
    |  『Arena』📍Posisi Player                               |
    |                                                        |
    |       ━━━━━━━━━Level 1━━━━━━━━━━━━━━━━━━━━━━━━━━━      |
    |       D       ┵                 |               |      |
    |       U       ┲                 |     "BOSS"    |      |
    |       N       |                 ┵     "BASE"    |      |
    |       G       |                 ┲               |      |
    |       E       |Level 2━━━━━━━━━━━━━━━━━━━━━━|━|━━      |
    |       O       |                   |             |      |
    |       N       |      "BOSS"       |             |      |
    |       ┵       |      "BASE"       ┵             |      |
    |               |                   ┲             |      |
    |       ┲       |Level 3━━|━  ━|━━━━━━━━━━━━━━━━━━━      |
    |       |       |               |                 |      |
    |       |       |               |                 |      |
    |       |       |               ┵                 |      |
    |       |       |                   "BOSS BASE"   |      |
    |       |       |               ┲                 |      |
    |       |       |               |                 |      |
    |       |       |               |                 |      |
    |       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|━━ ━━|━━━━      |
    |                                                        |
    |                                                        |
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    > Tekan Enter untuk memasuki Dungeon...

main()
    [Dungeon Telah Terbuka!]
    Memasuki Dungeon... Bersiap untuk bertarung!

    🔄 Menyiapkan Dungeon...
    ⏳ Mohon tunggu sebentar...
    ⚙️ Mempersiapkan lawan...

    ==============================

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        🔥 Level 1: Warrior 🔥
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Anda memasuki ruangan gelap dan mendengar langkah kaki... 
    ⚔️  Minion muncul! Bersiaplah untuk bertarung! ⚔️
    Kalahkan Para Kroco tersebut!🔥

    ♦️ Minion Tipe Assasin Sedang Menujumu!
    Serang!! ⚔️

    🔥  Minion memliki level yang lebih tinggi 🔥
    Jaga-jaga!

    🧩 Soal: Terdapat sebuah lingkaran dengan jari-jari {radius_2} cm, dan di dalamnya terdapat lingkaran dengan jari-jari {radius_1} cm berada di tengahnya, hitunglah luas daerah yang tidak tertutupi lingkaran yang lebih kecil:

    ==============================

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    🏰 Anda telah mencapai Boss Base!
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Anda telah melewati rintangan untuk datang ke sini! Saatnya menghadapi Boss Level Ini.
    Memasuki Ruang Boss...,
    🔥 Suara gemuruh memenuhi ruangan! Anda merasakan hawa panas yang semakin dekat.
    Sosok besar perlahan muncul dari kegelapan..., 0.

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    [Boss Warrior]: HIGH ORC 🪓
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    💬 HIGH ORC: "Siapa yang berani mengganggu kedamaian tempatku?! Bersiaplah untuk pertarunganmu!"
    💬 Kamu: "Aku tidak takut! Aku akan mengalahkanmu!!"

    > Tekan Enter untuk Bersiap Menyerang...
    🧩 Soal: "Sebuah taman berbentuk persegi panjang memiliki panjang {panjang} m dan lebar {lebar} m. Di tengahnya terdapat kolam berbentuk lingkaran dengan jari-jari {radius} m. Berapa luas taman yang tidak tertutupi kolam? (π = 3.14)": 
    ==============================
    = if jawaban benar
    ✔️ Jawaban benar
    ⚔️ Minion telah dikalahkan!
    🌟 Anda mendapatkan +EXP!

    = else ( jawaban salah)
    ❌ Jawaban salah!
    💔 Kamu terkena damage sebesar {damage} HP
    🩸 HP:〚{hp_bar}〛{player_hp}%
    🌟 Jawaban yang benar adalah jawaban

    = if player HP <= 0:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    🩸 HP:〚{hp_bar}〛{player_hp}%
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    💀 HP Anda habis! Game Over💀.

    🔥 Total EXP: {exp_level}
    ✔️ Total soal benar: {benar_level}
    ❌ Total soal salah: {salah_level}

    ==============================

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    📊  Statistik Akhir Permainan
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    ⚔️  Nama : {nama_player}
    🩸  HP Terakhir:〚{hp_bar}〛{player_hp}%
    🔥  Total EXP  : {total_exp}
    ✔️  Total soal benar: {soal_benar}
    ❌  Total soal salah: {soal_salah}

    🎉 Selamat {nama_player}
    Anda telah Mendapatkan Achievement! 
    🎖️ Achievement: {achievements[n]}! achievements = ("Novice Explorer", "Challenger", "The Conqueror", "Master of Dungeon")

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    🔥  HORMAT PADA SANG LEGENDA!, TUNDUKLAH PADA SANG RAJA! 👑
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            🔥 Kau Cukup Hebat Sebagai The Conqueror
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                🔥 Kau Cukup Terampil Juga Anak Muda
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Teruslah berlatih untuk mencapai gelar MASTER OF LEGEND!💪  
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ==============================
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                🔥  Terima Kasih Telah Bermain!               
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

***C. Kalkulator Bangun Datar: hitung.py***

    = Belajar Matematika: Geometri =
    = Menghitung Luas Bangun Datar =

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
    
    = if pilihan 1-6:  maka akan menjalankan fungsi masing-masing bangun datar yang sesuai dengan menu yang ditampilkan
    = elif pilihan 7: maka akan menampilkan histori atau tabel hasil dari perhitungan yang telah dilakukan user
    == Data Yang ditampilkan ==
    +-----------------+--------+
    | Bangun Datar    | Luas   |
    +-----------------+--------+
    | Segitiga        | 15.0   |
    | Persegi         | 25.0   |
    | ...             | ...    |
    +-----------------+--------+

    = elif pilihan 0: maka akan kembali ke menu utama di main.py
