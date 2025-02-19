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
