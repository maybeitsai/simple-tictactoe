from src.network import NetworkManager
from src.game_logic import TicTacToe
from src.ui import TicTacToeGUI
import threading
import time

class TicTacToeClient:
    def __init__(self):
        self.network = NetworkManager()
        self.game = TicTacToe()
        self.gui = TicTacToeGUI(self.game, self.network, self)
        self.player_symbol = None
        self.is_my_turn = False
    
    def connect_to_server(self):
        """Menghubungkan ke server"""
        if not self.network.connect_client():
            self.gui.show_message("Gagal terhubung ke server")
            return False
        
        # Terima simbol pemain dari server
        self.player_symbol = self.network.receive_data()
        self.gui.update_status(f"Anda bermain sebagai {self.player_symbol}")
        return True
    
    def start_game(self):
        """Memulai permainan"""
        # Thread untuk menerima update dari server
        receive_thread = threading.Thread(target=self.receive_updates)
        receive_thread.daemon = True
        receive_thread.start()
        
        self.gui.run()
    
    def receive_updates(self):
        """Menerima update permainan dari server"""
        while True:
            try:
                # Terima status permainan
                game_state = self.network.receive_data()
                
                if game_state:
                    # Cek apakah ada hasil akhir
                    if 'result' in game_state:
                        self.gui.show_message(game_state['result'])
                        break
                    
                    # Update papan permainan
                    self.game.board = game_state['board']
                    self.gui.update_board(game_state['board'])
                    
                    # Tentukan giliran
                    self.is_my_turn = game_state['current_player'] == self.player_symbol
                    
                    # Update status giliran
                    turn_message = "Giliran Anda" if self.is_my_turn else "Giliran Lawan"
                    self.gui.update_turn(turn_message)
                    
                    # Aktifkan/nonaktifkan tombol
                    self.gui.enable_buttons(self.is_my_turn)
            
            except Exception as e:
                print(f"Kesalahan menerima update: {e}")
                break
    
    def make_move(self, square):
        """Mengirim gerakan ke server"""
        if self.is_my_turn:
            # Kirim gerakan ke server
            if self.network.send_data(square):
                self.is_my_turn = False
                self.gui.enable_buttons(False)
                