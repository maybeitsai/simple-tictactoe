# Game Tic Tac Toe

## Project Overview

This project is an implementation of a network-based multiplayer Tic Tac Toe game which was developed as a project in the Jaringan Komputer subject. This project is designed to demonstrate fundamental concepts in network communications, socket programming, and client-server architecture using Python.

## Features

- Real-time multiplayer Tic Tac Toe
- Network-based gameplay
- Graphical user interface
- Turn-based game mechanics
- Winner detection
- Draw (tie) detection

## Prerequisites

- Python 3.9+
- UV (Universal Virtual Environment) package manager
- Tkinter (typically included with Python standard library)

## Project Structure

```
simple-tictactoe/
│
├── src/
│   ├── __init__.py
│   ├── server.py
│   ├── client.py
│   ├── network.py
│   ├── game_logic.py
│   └── ui.py
│
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Setup and Installation

### 1. Install UV Package Manager

```bash
# On Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. Clone the Repository

```bash
git clone https://github.com/maybeitsai/simple-tictactoe.git
cd simple-tictactoe
```

### 3. Create Virtual Environment and Synchronize Dependencies

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On Windows
.venv\Scripts\activate
# On Linux/macOS
source .venv/bin/activate

# Synchronize dependencies
uv sync
```

## Running the Game

### Start Server

```bash
uv run main.py server
```

### Start Client

```bash
uv run main.py client
```

### Multiple Players

1. Start the server on one machine
2. Start clients on different machines/terminals
3. Ensure both clients connect before playing

## Gameplay Instructions

- Two players can connect to the server
- Players are automatically assigned 'X' or 'O'
- Click on an empty square to make a move
- Wait for your turn
- First player to get 3 symbols in a row (horizontal, vertical, diagonal) wins
- Game ends with a win or draw

## Network Configuration

- Default Host: `localhost`
- Default Port: `17804`

To change network settings, modify `NetworkManager` in `network.py`

## Troubleshooting

### Common Issues

1. **Connection Failure**
   - Check if server is running
   - Verify network settings
   - Ensure firewall allows connections

2. **GUI Not Responding**
   - Restart the application
   - Check Python and Tkinter installation

## Development

### Running Tests

```bash
# No tests configured. Recommend adding unit tests for:
# - Game Logic
# - Network Communication
# - UI Interactions
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Harry Mardika - harrymardika@student.gunadarma.ac.id

Project Link: [https://github.com/maybeitsai/simple-tictactoe](https://github.com/maybeitsai/simple-tictactoe)

## Acknowledgments

- Tkinter for GUI
- Python Standard Library
- UV Package Manager