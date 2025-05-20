# 🖧 Aplikasi Socket Python (+ GUI Tkinter)

Aplikasi chat sederhana berbasis TCP menggunakan modul `socket`, `threading`, dan `tkinter` dari Python. Proyek ini mencakup aplikasi GUI untuk **server** dan **client** yang dapat saling mengirim dan menerima pesan secara real-time melalui socket TCP.

---

## 📦 Fitur

- 🔁 Komunikasi dua arah antara server dan client (TCP full-duplex)
- 🖥️ Antarmuka pengguna sederhana menggunakan `tkinter`
- 📝 Log pesan ditampilkan di GUI dan terminal
- 🔄 Multithreading: pesan diterima tanpa memblokir GUI
- 🧪 Berjalan di sistem lokal (`localhost`)

---

## ▶️ Running App

### 1. Requirement

Pastikan Python 3.x sudah terinstal.

### 2. Jalankan Server

```bash
python tcp_server.py
```

- GUI server akan muncul dan menunggu koneksi dari client.

### 3. Jalankan Client (di terminal lain)

```bash
python tcp_client.py
```

- GUI client akan muncul dan langsung mencoba koneksi ke server di `127.0.0.1:9000`.

---

## ⚙️ Penjelasan Teknis

### `TCP_SERVER.py`
- Membuat socket TCP: `socket(AF_INET, SOCK_STREAM)`
- Melakukan binding ke `127.0.0.1:9000` dan mendengarkan koneksi masuk
- Menerima pesan di thread terpisah
- Mengirim pesan melalui GUI (Entry + tombol Kirim)
- Log pesan tampil di GUI dan terminal

### `TCP_CLIENT.py`
- Menghubungkan ke server di `127.0.0.1:9000`
- Memulai thread untuk terus menerima pesan dari server
- Mengirim pesan melalui GUI (Entry + tombol Kirim)
- Log pesan tampil di GUI dan terminal

### Protokol Komunikasi
- Menggunakan `sendall()` dan `recv()` dengan buffer 1024 byte
- Protokol TCP menjamin pengiriman pesan secara andal dan berurutan

---

## 🛡️ Penanganan Error

- Kegagalan koneksi akan ditampilkan di GUI client
- Exception pada `recv()` ditangani agar thread tidak crash
- Operasi socket dan thread dibungkus dengan `try-except`

---

## ✅ Dependencies

Tidak perlu menginstal modul tambahan. Semua menggunakan pustaka standar Python:

- `socket`
- `threading`
- `tkinter`
- `tkinter.scrolledtext`