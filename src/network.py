import socket
import json
import threading
import time

class NetworkManager:
    def __init__(self, host='localhost', port=17804):
        self.host = host
        self.port = port
        self.socket = None
        self.is_connected = False
        self.connection = None
    
    def start_server(self):
        """Memulai server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(2)
        print(f"Server berjalan di {self.host}:{self.port}")
    
    def connect_client(self):
        """Menghubungkan client ke server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
            self.is_connected = True
            print(f"Terhubung ke server {self.host}:{self.port}")
        except Exception as e:
            print(f"Gagal terhubung: {e}")
            return False
        return True
    
    def accept_connection(self):
        """Menerima koneksi dari client"""
        self.connection, address = self.socket.accept()
        print(f"Koneksi diterima dari {address}")
        return self.connection
    
    def send_data(self, data, connection=None):
        """Mengirim data melalui socket"""
        try:
            socket_to_use = connection if connection else self.socket
            message = json.dumps(data).encode('utf-8')
            socket_to_use.send(message)
        except Exception as e:
            print(f"Kesalahan mengirim data: {e}")
            return False
        return True
    
    def receive_data(self, connection=None):
        """Menerima data dari socket"""
        try:
            socket_to_use = connection if connection else self.socket
            data = socket_to_use.recv(1024).decode('utf-8')
            return json.loads(data)
        except Exception as e:
            print(f"Kesalahan menerima data: {e}")
            return None
    
    def close_connection(self):
        """Menutup koneksi"""
        if self.socket:
            self.socket.close()
        if self.connection:
            self.connection.close()
        self.is_connected = False