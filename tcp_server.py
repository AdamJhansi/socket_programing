import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9000))
    server_socket.listen(1)
    log.insert(tk.END, "Menunggu koneksi client...\n")
    print("Menunggu koneksi client...")

    conn, addr = server_socket.accept()
    log.insert(tk.END, f"Terhubung dengan {addr}\n")
    print(f"Terhubung dengan {addr}")

    def receive():
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break
                log.insert(tk.END, f"Client: {data}\n")
                print(f"Client: {data}")
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    def send_message():
        msg = entry.get()
        conn.sendall(msg.encode())
        log.insert(tk.END, f"Server: {msg}\n")
        print(f"Server: {msg}")
        entry.delete(0, tk.END)

    send_btn.config(command=send_message)

window = tk.Tk()
window.title("TCP Server")

log = ScrolledText(window, width=50, height=20)
log.pack()

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT)

send_btn = tk.Button(window, text="Kirim")
send_btn.pack(side=tk.LEFT)

threading.Thread(target=start_server, daemon=True).start()

window.mainloop()
