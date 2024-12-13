# Square Root Guessing Game

This is a web-based game where users try to guess the square root of a random number.

## Features
- Random number generation between 50 and 250
- Configurable accuracy requirement
- Guess tracking and feedback
- Interactive web interface
- Play again functionality

## Setup on Mac

1. Open Terminal on your Mac
2. Install pip if you haven't already:
   ```
   python -m ensurepip --upgrade
   ```
3. Create a new virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
5. Install Flask:
   ```
   pip install -r requirements.txt
   ```
6. Run the application:
   ```
   python app.py
   ```
7. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## How to Play

1. Set your desired accuracy percentage
2. Click "Pick a random number" to start
3. Enter your guess for the square root
4. Receive feedback on whether your guess is too high or too low
5. Continue until you get the correct answer
6. Click "Play Again" to start a new game