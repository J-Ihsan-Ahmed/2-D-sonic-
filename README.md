# Sonic Platformer Game

A simple platformer game where the player controls Sonic (or a character of your choice), dodging obstacles and collecting points while avoiding collision with moving obstacles.

## Features:
- **Double Jump**: The player can perform a double jump in the air.
- **Scrolling Background**: The background scrolls to create a dynamic running environment.
- **Obstacles**: Random obstacles appear in the player's path that must be avoided.
- **Score**: The score increases as the player survives, and the highest score is tracked.
- **Game Over and Restart**: On collision with an obstacle, the player is given the option to restart the game.

## Requirements:
- Python 3.x
- Pygame library

## Installation:

1. **Install Python**: Make sure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Install Pygame**:
    ```bash
    pip install pygame
    ```

3. **Download the Game Files**:
    - Clone or download the repository to your local machine.
    - Ensure you have the Sonic image and background image stored at the specified paths in the code. If not, update the paths to match where your images are located.

4. **Game Setup**:
    - Make sure to place the game image files (Sonic image and background) at the specified paths in the code:
      - `sonic_img_path = "C:\\Users\\Dell\\Downloads\\image-removebg-preview.png"`
      - `background_img_path = "C:\\Users\\Dell\\Downloads\\sonic bg.png"`
    - If the images are stored elsewhere, update the paths in the code to point to the correct directory.

## How to Play:

1. Run the Python script:
    ```bash
    python sonic_game.py
    ```
2. Use the **Left Arrow** and **Right Arrow** keys to move Sonic.
3. Press the **Spacebar** to perform a jump (and double jump).
4. Avoid the red obstacles that come towards you.
5. The score increases as long as you avoid obstacles. The game will end when you collide with an obstacle, and you can restart by pressing **'R'**.

## Key Bindings:
- **Left Arrow**: Move Sonic left.
- **Right Arrow**: Move Sonic right.
- **Spacebar**: Make Sonic jump (double jump possible).
- **R**: Restart the game after a game over.

## Game Over:
- When you collide with an obstacle, the game ends, and you can restart by pressing the **R** key.

## Customization:
- **Obstacles**: You can adjust the speed and gap between obstacles by modifying the values of `OBSTACLE_GAP` and `speed` inside the `Obstacle` class.
- **Player Movement**: You can adjust the player’s velocity and jumping behavior by modifying the `PLAYER_VEL` and jump parameters.

## Credits:
- **Images**: You can customize the Sonic character and background images by placing your own image files in the correct paths.
- **Code**: Written by [Your Name], based on a simple Pygame template.

## License:
This project is open source and available under the [MIT License](LICENSE).
