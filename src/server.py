from src.network import NetworkManager
from src.game_logic import TicTacToe
import threading
import json
import time

class TicTacToeServer:
    def __init__(self):
        self.network = NetworkManager()
        self.game = TicTacToe()
        self.clients = []
        self.client_symbols = {}
        self.current_player = 'X'
        self.game_started = False
    
    def start_server(self):
        """Memulai server dan menunggu koneksi"""
        self.network.start_server()
        
        # Tunggu 2 client terhubung
        while len(self.clients) < 2:
            client_socket = self.network.accept_connection()
            self.clients.append(client_socket)
            
            # Berikan simbol kepada client
            symbol = 'X' if len(self.clients) == 1 else 'O'
            self.client_symbols[client_socket] = symbol
            self.network.send_data(symbol, client_socket)
        
        # Mulai thread untuk menangani permainan
        game_thread = threading.Thread(target=self.manage_game)
        game_thread.start()
    
    def manage_game(self):
        """Mengelola alur permainan"""
        # Kirim status awal permainan
        self.broadcast_game_state()
        
        while True:
            try:
                # Tunggu gerakan dari client saat ini
                current_client = self.clients[0] if self.current_player == 'X' else self.clients[1]
                move = self.network.receive_data(current_client)
                
                if move is not None:
                    # Validasi dan proses gerakan
                    if self.game.make_move(move, self.current_player):
                        # Cek status permainan
                        if self.game.winner(move, self.current_player):
                            self.broadcast_result(f"Pemain {self.current_player} menang!")
                            break
                        
                        if self.game.is_board_full():
                            self.broadcast_result("Permainan seri!")
                            break
                        
                        # Ganti giliran
                        self.current_player = 'O' if self.current_player == 'X' else 'X'
                        
                        # Broadcast status permainan
                        self.broadcast_game_state()
            
            except Exception as e:
                print(f"Kesalahan dalam permainan: {e}")
                break
    
    def broadcast_game_state(self):
        """Mengirim status papan permainan ke semua client"""
        game_state = {
            'board': self.game.board,
            'current_player': self.current_player
        }
        
        for client in self.clients:
            self.network.send_data(game_state, client)
    
    def broadcast_result(self, message):
        """Mengirim hasil akhir permainan"""
        for client in self.clients:
            self.network.send_data({'result': message}, client)
