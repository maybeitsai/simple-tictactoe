import tkinter as tk
from tkinter import messagebox, ttk
import threading

class TicTacToeGUI:
    def __init__(self, game_logic, network_manager, client_instance):
        self.game = game_logic
        self.network = network_manager
        self.client = client_instance

        # Create main window with modern styling
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe Online")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')

        # Custom font
        self.title_font = ('Arial', 24, 'bold')
        self.label_font = ('Arial', 12)
        self.button_font = ('Arial', 20, 'bold')

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        self.title_label = tk.Label(
            self.main_frame, 
            text="Online Tic Tac Toe", 
            font=self.title_font, 
            bg='#f0f0f0', 
            fg='#333333'
        )
        self.title_label.pack(pady=(0, 20))

        # Status and turn labels with improved styling
        self.status_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.status_frame.pack(pady=10)

        self.status_label = tk.Label(
            self.status_frame, 
            text="Waiting for Opponent...", 
            font=self.label_font, 
            bg='#f0f0f0', 
            fg='#666666'
        )
        self.status_label.pack(side='left', padx=10)

        self.turn_label = tk.Label(
            self.status_frame, 
            text="", 
            font=self.label_font, 
            bg='#f0f0f0', 
            fg='#007bff'
        )
        self.turn_label.pack(side='right', padx=10)

        # Game board with improved design
        self.board_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.board_frame.pack(pady=20)

        self.buttons = []
        self.create_board()

        # Styling
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Modern theme
        self.style.configure('TButton', 
            font=self.button_font, 
            background='white', 
            foreground='#333333',
            borderwidth=2,
            relief='raised'
        )
        self.style.map('TButton',
            background=[('active', '#e0e0e0')],
            foreground=[('active', 'black')]
        )

    def create_board(self):
        """Create game board with improved design"""
        for i in range(3):
            for j in range(3):
                btn = ttk.Button(
                    self.board_frame, 
                    text='', 
                    width=10, 
                    command=lambda x=i*3+j: self.on_click(x),
                    style='TButton'
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(btn)

    def on_click(self, square):
        """Handle button click"""
        self.client.make_move(square)

    def update_board(self, board_state):
        """Update board display with color-coded moves"""
        for i, state in enumerate(board_state):
            if state == 'X':
                self.buttons[i]['text'] = state
                self.buttons[i]['style'] = 'X.TButton'
                self.style.configure('X.TButton', 
                    foreground='#007bff',  # Blue for X
                    font=self.button_font
                )
            elif state == 'O':
                self.buttons[i]['text'] = state
                self.buttons[i]['style'] = 'O.TButton'
                self.style.configure('O.TButton', 
                    foreground='#dc3545',  # Red for O
                    font=self.button_font
                )
            else:
                self.buttons[i]['text'] = ''
                self.buttons[i]['style'] = 'TButton'

    def update_status(self, message):
        """Update game status"""
        self.status_label.config(text=message)

    def update_turn(self, turn_message):
        """Update turn information"""
        self.turn_label.config(text=turn_message)

    def enable_buttons(self, enable=True):
        """Enable/disable buttons"""
        state = 'normal' if enable else 'disabled'
        for btn in self.buttons:
            btn['state'] = state

    def show_message(self, message):
        """Display game result with custom style"""
        messagebox.showinfo(
            "Game Over", 
            message, 
            icon=messagebox.INFO
        )
        self.root.quit()

    def run(self):
        """Run the GUI"""
        self.root.mainloop()