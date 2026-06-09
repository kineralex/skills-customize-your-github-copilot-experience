# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python by using strings, loops, conditionals, and user input to track guesses and reveal a hidden word.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Create the core variables and word selection needed to start the game.

#### Requirements
Completed program should:

- Choose a secret word at random from a predefined list.
- Start with an empty list of guessed letters and a counter for incorrect guesses.
- Set a maximum number of incorrect guesses for the game.

### 🛠️ Build the Gameplay Loop

#### Description
Implement the main loop that lets the player guess letters, updates the display, and ends the game when the word is solved or attempts are exhausted.

#### Requirements
Completed program should:

- Ask the player to enter one letter at a time.
- Show the current progress of the word using underscores for unrevealed letters.
- Track guessed letters so the player can see what has already been used.
- Increase the incorrect guess count when a letter is not in the word.
- End the game with a win message when the word is fully guessed.
- End the game with a lose message when the maximum number of incorrect guesses is reached.
