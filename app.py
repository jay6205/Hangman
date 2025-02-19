from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "hangman_secret_key" # this is used for session storage

def load_words():
    with open("words.txt", "r") as file:
        words = file.readlines()
    return words

@app.route("/",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    words = load_words()
    session["word"] = random.choice(words).upper().strip()
    session["word_display"] = "_" * len(session["word"])
    session["guesses"] = []
    session["allowed_errors"] = 7
    return render_template("game.html", word_display=session["word_display"], allowed_errors=session["allowed_errors"], guesses=session["guesses"], game_over=False)

@app.route("/guess", methods=["POST"])
def guess():
    if "word" not in session:
        return redirect(url_for("game"))
    
    guess = request.form["guess"].upper()
    if guess in session["guesses"] or not guess.isalpha() or len(guess) != 1:
        return redirect(url_for("game"))
    
    session["guesses"].append(guess)
    
    if guess not in session["word"]:
        session["allowed_errors"] -= 1
    
    session["word_display"] = "".join([letter if letter in session["guesses"] else "_" for letter in session["word"]])
    
    game_over = session["allowed_errors"] == 0 or "_" not in session["word_display"]
    return render_template("game.html", word_display=session["word_display"], allowed_errors=session["allowed_errors"], guesses=session["guesses"], game_over=game_over, word=session["word"] if game_over else None)

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect(url_for("game"))

if __name__ == "__main__":
    app.run(debug=True)
