# 🐢 Turtle Crossing Game

A fun Python implementation of a road-crossing game using the Turtle graphics module.

![Turtle Crossing](https://img.shields.io/badge/Game-Turtle%20Crossing-brightgreen)
![Python](https://img.shields.io/badge/Language-Python-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📝 Description

This project is an arcade-style game where the player controls a turtle that must cross a busy road filled with moving cars. The player must navigate the turtle safely to the other side without colliding with any vehicles. As the player advances through levels, the cars move faster, making the game progressively more challenging.

## ✨ Features

- Intuitive turtle movement controls
- Randomly generated cars with varying colors
- Progressive difficulty with increasing levels
- Score tracking with level display
- Collision detection
- Game over functionality

## 🕹️ Controls

- **Move Turtle Forward**: Up Arrow Key

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/turtle-crossing.git
cd turtle-crossing
```

2. Make sure you have Python installed. This game was developed using Python 3.

3. No additional dependencies are required as the game uses the built-in Turtle graphics library.

## 🎮 How to Play

Run the main script:
```bash
python main.py
```

- The turtle starts at the bottom of the screen
- Use the Up Arrow key to move the turtle forward
- Avoid colliding with cars crossing the screen
- Reach the top of the screen to advance to the next level
- Cars move faster with each level
- The game ends if the turtle collides with a car

## 🏗️ Project Structure

- `main.py`: Main game script that initializes the screen, turtle (player), cars, and scoreboard and runs the game loop
- `player.py`: Contains the `Player` class that handles turtle creation and movement
- `car_manager.py`: Contains the `CarManager` class that creates and moves the cars
- `scoreboard.py`: Contains the `Scoreboard` class that tracks and displays the level information

## 📋 Development Process

The game was developed following these steps:

1. ✅ Create the game screen and basic controls
2. ✅ Implement the player (turtle) movement
3. ✅ Create and animate multiple car objects
4. ✅ Detect collision between the turtle and cars
5. ✅ Implement scoreboard to track level progress
6. ✅ Reset turtle position after successfully crossing
7. ✅ Increase difficulty with each level

## 🐛 Known Issues

- The turtle collision detection with cars is not working correctly (currently in TODO list)
- Cars are generated randomly which occasionally creates difficult patterns

## 🔜 Future Improvements

- Fix collision detection between turtle and cars
- Add different types of obstacles
- Implement lives system
- Add power-ups (e.g., temporary invincibility, slow down cars)
- Create a start screen with game instructions
- Add sound effects and background music
- Implement high score tracking

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👏 Acknowledgements

- Inspired by classic arcade crossing games
- Built using Python's Turtle graphics library
