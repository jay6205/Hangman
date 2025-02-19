Hangman Game (Flask + Jinja2)

📌 Overview

This is a simple Hangman game built using Flask and Jinja2 templates, with a clean frontend designed using HTML and CSS. The game randomly selects a word from a file (words.txt) and challenges the player to guess it before running out of attempts!

🎮 Features

🔤 Random word selection from words.txt

✅ Dynamic word display updating with each correct guess

❌ Limited incorrect attempts before the game ends

📄 Separate pages for home screen and game interface

🔄 Restart option for a new game

🖥️ Flask-powered backend with Jinja2 templating

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/hangman-game.git
cd hangman-game

2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

3️⃣ Install Dependencies

pip install flask

4️⃣ Run the Flask App

python app.py

5️⃣ Open in Browser

Visit http://127.0.0.1:5000 in your web browser to start playing!

📂 Project Structure

/hangman-game
│-- /static
│   ├── styles.css   # CSS file for styling
│-- /templates
│   ├── index.html   # Home screen
│   ├── game.html    # Game interface
│-- app.py           # Flask application
│-- words.txt        # List of words for the game
│-- README.md        # Project documentation

🚀 How to Play

Click 'Start Game' on the home screen.

Enter a letter and click 'Submit' to make a guess.

If the letter is in the word, it will be revealed.

If not, an incorrect guess is recorded.

You win if you guess the word before using all attempts!

Click 'Restart' to play again.
