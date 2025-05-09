# DON-Destroyer-of-Numbers-Game

This is a simple text-based game where players fight enemies and try to survive through multiple attempts. The game generates random enemies and life scores for the player, and the player's goal is to defeat enemies without losing all their life points.

## How to Play

1. Run the game script.
2. Enter your name when prompted.
3. The game will generate a random life score and a list of enemies for each attempt.
4. Select a number from the list of enemies to fight:
   - If the selected number is less than or equal to your life score, you win the fight, and your life score increases.
   - If the selected number is greater than your life score, you lose the game.
5. The game ends after 20 attempts or if you lose a fight.

## Features

- **Random Life Score**: Each player starts with a random life score between 1 and 50.
- **Dynamic Enemies**: Enemies become stronger as the game progresses:
  - Attempts 1–5: Enemies have values between 15 and 100.
  - Attempts 6–10: Enemies have values between 250 and 2000.
  - Attempts 11–15: Enemies have values between 3000 and 10000.
  - Attempts 16–20: Enemies have values between 20000 and 100000.
- **Game Statistics**: After the game ends, a text file is generated with the following details:
  - Player name
  - Number of attempts
  - List of enemies presented
  - The number selected by the player
  - Whether the player won or lost
  - Final life score

## How to Run

1. Ensure you have Python installed on your system.
2. Save the script as `Code of The Game.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the following command:
   ```sh
   python "Code of The Game.py"
