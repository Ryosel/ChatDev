# Minesweeper Game User Manual

## Introduction

Welcome to the Minesweeper Game! This user manual will guide you through the installation process and explain how to use and play the game.

## Installation

To install the Minesweeper Game, you need to follow these steps:

1. Make sure you have Python installed on your computer. If not, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you have downloaded the game files.

3. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the Pygame library, which is necessary to run the game.

## Usage

To start the Minesweeper Game, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you have downloaded the game files.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. The game window will open, and you will see the Minesweeper board.

4. Use the mouse to click on a cell to reveal its content. The goal of the game is to avoid clicking on a mine. If you click on a mine, you lose the game.

5. If you reveal a cell without a mine, it will show a number indicating the number of adjacent cells that contain mines. Use this information to strategically reveal cells and avoid mines.

6. To mark a cell as a potential mine, right-click on it. This will place a flag on the cell.

7. Continue revealing cells and marking potential mines until you have revealed all non-mine cells. If you successfully reveal all non-mine cells, you win the game.

8. After the game ends, you can choose to play again by closing the game window and running the `python main.py` command again.

## Conclusion

Congratulations! You have successfully installed and learned how to use the Minesweeper Game. Enjoy playing and have fun! If you have any further questions or need assistance, please don't hesitate to reach out to our support team.