import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    try:
        client_socket.connect(('127.0.0.1', 9000))
        log.insert(tk.END, "Terhubung ke server...\n")
        print("Terhubung ke server...")

        def receive():
            while True:
                try:
                    data = client_socket.recv(1024).decode()
                    if not data:
                        break
                    log.insert(tk.END, f"Server: {data}\n")
                    print(f"Server: {data}")
                except:
                    break

        threading.Thread(target=receive, daemon=True).start()
    except Exception as e:
        log.insert(tk.END, f"Error: {e}\n")
        print(f"Error: {e}")

def send_message():
    msg = entry.get()
    client_socket.sendall(msg.encode())
    log.insert(tk.END, f"Client: {msg}\n")
    print(f"Client: {msg}")
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("TCP Client")

log = ScrolledText(window, width=50, height=20)
log.pack()

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT)

send_btn = tk.Button(window, text="Kirim", command=send_message)
send_btn.pack(side=tk.LEFT)

connect()

window.mainloop()
