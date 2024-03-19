```markdown
# Zombie Shooter Game Manual

Welcome to the Zombie Shooter Game, a thrilling top-down 2D roguelike shooting game where you must survive against hordes of relentless zombies. This manual will guide you through the main functions of the software, how to install environment dependencies, and how to play the game.

## Installation

Before you can start playing the Zombie Shooter Game, you need to ensure that you have Python and Pygame installed on your system. Follow the steps below to set up your environment:

### Python Installation

If you don't have Python installed, download and install it from the official Python website:

[Python Download](https://www.python.org/downloads/)

### Pygame Installation

Pygame is a set of Python modules designed for writing video games. Install Pygame using pip with the following command:

```bash
pip install pygame
```

Alternatively, you can install Pygame using the requirements file provided with the game:

```bash
pip install -r requirements.txt
```

## How to Play

Once you have installed all the necessary dependencies, you can start playing the game by running the `main.py` script.

### Starting the Game

Navigate to the game directory in your terminal or command prompt and execute the following command:

```bash
python main.py
```

### Game Controls

- **Movement**: Use the `W`, `A`, `S`, `D` keys to move your character up, left, down, and right, respectively.
- **Shooting**: Click the left mouse button to shoot bullets in the direction of the cursor.

### Objective

Your goal is to survive as long as possible by avoiding zombies and shooting them down. The zombies will continuously chase you, and the game ends when a zombie touches your character.

### Tips

- Keep moving to avoid being cornered by zombies.
- Aim carefully and conserve your bullets.
- Use obstacles to your advantage to create distance between you and the zombies.

## Main Functions

- **Player Movement**: The player can freely move around the game area to dodge zombies.
- **Shooting Mechanism**: The player can shoot bullets towards the mouse cursor to eliminate zombies.
- **Zombie AI**: Zombies will chase the player with a basic AI algorithm.
- **Collision Detection**: The game detects collisions between the player, zombies, and bullets.
- **Game Over Condition**: The game ends when the player is touched by a zombie.

## Support

If you encounter any issues or have questions about the game, please feel free to reach out for support.

Enjoy the game and try to survive the zombie apocalypse!
```

This manual provides a comprehensive guide for users to install, play, and understand the main functions of the Zombie Shooter Game. It is written in Markdown format for easy reading and can be converted to other formats if needed.