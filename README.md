# NumBuster
**NumBuster** adalah alat Python yang mengambil informasi publik terkait nomor telepon melalui API CallerProtect. Dengan alat ini, Anda dapat dengan cepat mengetahui detail seperti penyedia layanan, wilayah, dan profil terkait nomor tersebut.

![NumBuster](https://github.com/user-attachments/assets/6f162b7a-6808-4011-84c1-77df1c82fed8)

> **Peringatan:** NumBuster hanya untuk tujuan edukasi. Gunakan dengan bijak dan hormati privasi.

## Fitur
- Mendapatkan nama lengkap (jika tersedia) dari nomor telepon.
- Menampilkan operator dan region nomor telepon.
- Menyediakan tautan untuk melihat profil lebih lanjut (jika ada).

## Cara Kerja
NumBuster menggunakan API dari `callerprotect.de` untuk mengambil data terkait nomor telepon. Program ini secara otomatis memformat nomor telepon sesuai dengan format internasional sebelum mengirimkan permintaan pencarian.

## Persyaratan
- Library Python:
  - `requests`
  - `json`
- Python 3.x

Untuk menginstal library yang diperlukan, jalankan perintah berikut:
```bash
pip install requests
```

## Cara Penggunaan
1. Clone repositori ini:
    ```bash
    git clone https://github.com/RozhakXD/NumBuster.git
    ```
2. Masuk ke direktori proyek:
    ```bash
    cd NumBuster
    ```
3. Jalankan script Python:
    ```bash
    python Run.py
    ```
4. Masukkan nomor telepon yang ingin Anda cari (gunakan format internasional, tanpa tanda "+" atau spasi):
    ```bash
    Enter Phone Number: 6281234567890
    ```

## Contoh Output
```yaml
================= PROFILE PUBLIK =================

Nama Lengkap     : John Doe
Tautan           : https://callerprotect.de/profile/12345
Carrier          : Telkomsel
Region           : Jakarta
Phone Number     : 6281234567890
```

## Tangkapan Layar
![FunPic_20240921](https://github.com/user-attachments/assets/7937c2e8-d65f-488a-a48b-077b6e924e94)

## Dukungan
Jika Anda merasa proyek ini bermanfaat dan ingin mendukung pengembangan lebih lanjut, Anda bisa memberikan donasi melalui:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

## Catatan
- Pastikan Anda mengganti token API dengan token yang valid di parameter `access_token` pada fungsi `callerprotect`.
- Program ini mengandalkan data yang tersedia secara publik dan tidak menjamin kelengkapan atau keakuratan informasi.

## Kontribusi
Kami menerima kontribusi dari komunitas! Jika Anda ingin menambahkan fitur baru atau memperbaiki bug, silakan fork repositori ini dan kirimkan pull request.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](https://github.com/RozhakXD/NumBuster?tab=MIT-1-ov-file).
