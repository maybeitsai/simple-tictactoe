import sys
from src.server import TicTacToeServer
from src.client import TicTacToeClient

def main():
    if len(sys.argv) < 2:
        print("Gunakan: python main.py [server/client]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == 'server':
        server = TicTacToeServer()
        server.start_server()
    elif mode == 'client':
        client = TicTacToeClient()
        if client.connect_to_server():
            client.start_game()
    else:
        print("Mode tidak valid. Gunakan 'server' atau 'client'.")

if __name__ == "__main__":
    main()