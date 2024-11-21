class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(9)]
        self.current_winner = None
    
    def make_move(self, square, letter):
        """Melakukan langkah pada papan permainan"""
        if self.board[square] == '':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        """Memeriksa pemenang berdasarkan baris, kolom, dan diagonal"""
        # Cek baris
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # Cek kolom
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Cek diagonal
        diagonals = [
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]]
        ]
        
        for diag in diagonals:
            if all([spot == letter for spot in diag]):
                return True
        
        return False
    
    def is_board_full(self):
        """Memeriksa apakah papan penuh"""
        return '' not in self.board
    
    def empty_squares(self):
        """Mengembalikan kotak kosong"""
        return [i for i, spot in enumerate(self.board) if spot == '']
    
    def num_empty_squares(self):
        """Menghitung jumlah kotak kosong"""
        return len(self.empty_squares())
    
    def reset_game(self):
        """Reset permainan"""
        self.board = ['' for _ in range(9)]
        self.current_winner = None