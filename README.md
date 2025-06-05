# Ping Pong Game

This repository contains a simple terminal-based ping pong game implemented in Python using the built-in `curses` module.

## Controls
- **a**: move your paddle up
- **d**: move your paddle down
- **q**: quit the game

The right paddle is controlled by the computer with a very small chance to miss the ball.

## Running the Game
1. Open a terminal window on your machine (Linux, macOS, or Windows Subsystem for Linux).
2. Change into the directory containing `ping_pong.py`.
3. Run the game with the command below:

```bash
python3 ping_pong.py
```

The game uses `curses`, so it must be run in an interactive terminal. If you
execute it in a headless environment (such as some containers), the display will
not appear.
