# 🖧 TCP Chat App (Python Socket Programming + Tkinter GUI)

A simple TCP-based chat application using Python's `socket`, `threading`, and `tkinter` modules. This project includes both **server** and **client** GUI applications that can send and receive messages in real-time using TCP sockets.

---

## 📦 Fitur

- Komunikasi dua arah antara server dan client (TCP full-duplex)
- GUI sederhana menggunakan `tkinter`
- Log pesan ditampilkan di GUI dan juga di terminal
- Multithreaded: pesan bisa diterima tanpa memblokir GUI
- Kompatibel di sistem lokal (`localhost`)

---

## 🗂️ Struktur Project

tcp_chat_app/
├── TCP_SERVER.py # GUI aplikasi server
├── TCP_CLIENT.py # GUI aplikasi client
└── README.md # Dokumentasi ini

yaml
Copy
Edit

---

## ▶️ Cara Menjalankan Aplikasi

### 1. Pastikan Python sudah terinstall (Python 3.x)

### 2. Jalankan server terlebih dahulu:

```bash
python TCP_SERVER.py
GUI server akan muncul dan menunggu koneksi client.

3. Jalankan client di terminal lain:
bash
Copy
Edit
python TCP_CLIENT.py
GUI client akan muncul dan langsung mencoba koneksi ke server di 127.0.0.1:9000.

📷 Contoh Tampilan
GUI Server
vbnet
Copy
Edit
[GUI Text Area]
Server: Hai client!
Client: Halo server!
GUI Client
vbnet
Copy
Edit
[GUI Text Area]
Client: Halo server!
Server: Hai client!
⚙️ Penjelasan Teknis
TCP_SERVER.py
Membuat socket TCP (socket.AF_INET, socket.SOCK_STREAM)

Binding ke 127.0.0.1:9000 dan menunggu client

Menerima pesan dari client dalam thread terpisah

Mengirim pesan lewat GUI (entry + tombol Kirim)

Log ditampilkan di GUI (ScrolledText) dan console (print())

TCP_CLIENT.py
Menginisiasi koneksi ke server 127.0.0.1:9000

Setelah terhubung, mulai thread untuk mendengarkan pesan dari server

Kirim pesan lewat GUI client (entry + tombol Kirim)

Log juga ditampilkan di GUI dan console

Komunikasi
Menggunakan sendall() dan recv() dengan buffer 1024 byte

Protokol TCP: memastikan koneksi andal, pesan sampai berurutan

🛡️ Penanganan Error
Koneksi gagal akan ditampilkan di GUI client

Exception pada recv() ditangani agar thread tidak crash

Gunakan try-except pada bagian socket dan thread

✅ Dependencies
Tidak perlu install paket eksternal. Semua menggunakan modul standar Python:

socket

threading

tkinter

tkinter.scrolledtext