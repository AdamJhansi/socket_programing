
# 🖧 TCP Chat App (Python Socket Programming + Tkinter GUI)

A simple TCP-based chat application built with Python’s `socket`, `threading`, and `tkinter` modules. The project includes both **server** and **client** GUI programs that support real-time messaging over TCP sockets.

---

## 📦 Features

- 🔁 Full-duplex communication between server and client (TCP)
- 🖥️ Simple GUI using `tkinter`
- 📝 Message logs shown in both GUI and terminal
- 🔄 Multithreaded: message receiving runs without blocking the GUI
- 🧪 Works on local system (`localhost`)

---

## ▶️ How to Run

### 1. Prerequisites

Ensure Python 3.x is installed on your system.

### 2. Run the Server

```bash
python TCP_SERVER.py
```

- A GUI window for the server will appear and wait for incoming client connections.

### 3. Run the Client (in another terminal)

```bash
python TCP_CLIENT.py
```

- The client GUI will open and attempt to connect to the server at `127.0.0.1:9000`.

---

## 🖼️ Example Screenshots

### Server GUI
```
[Text Area Output]
Server: Hai client!
Client: Halo server!
```

### Client GUI
```
[Text Area Output]
Client: Halo server!
Server: Hai client!
```

---

## ⚙️ Technical Overview

### `TCP_SERVER.py`
- Creates a TCP socket: `socket(AF_INET, SOCK_STREAM)`
- Binds to `127.0.0.1:9000` and listens for client connections
- Handles incoming messages in a separate thread
- Sends messages through the GUI (Entry + Send button)
- Logs messages in GUI (ScrolledText) and terminal

### `TCP_CLIENT.py`
- Connects to server at `127.0.0.1:9000`
- Starts a thread to continuously receive messages from the server
- Sends messages through the GUI (Entry + Send button)
- Logs messages in GUI and terminal

### Communication Protocol
- Uses `sendall()` and `recv()` with a 1024-byte buffer
- TCP ensures reliable and ordered delivery of messages

---

## 🛡️ Error Handling

- Connection failures are shown in the client GUI
- Exceptions during `recv()` are caught to prevent thread crashes
- All socket and thread operations are wrapped in `try-except` blocks

---

## ✅ Dependencies

All modules used are part of Python’s standard library — no external installation needed:

- `socket`
- `threading`
- `tkinter`
- `tkinter.scrolledtext`

---

## 📁 Project Structure

```
📦 tcp_chat_app/
├── TCP_SERVER.py      # Server-side GUI app
├── TCP_CLIENT.py      # Client-side GUI app
└── README.md          # Project documentation
```

---

## 📌 Notes

- This application is intended for **local use only** (`127.0.0.1`). To use over a network, configure IP and firewall accordingly.
- Great for learning the basics of **socket programming** and **multithreaded GUI apps** in Python.

---

## 🧑‍💻 Author

Created with ❤️ using Python and Tkinter.
