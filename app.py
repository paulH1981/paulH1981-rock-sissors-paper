import random
from flask import (Flask, render_template, request, jsonify)

app = Flask(__name__)


@app.route('/')
def index():
    print('Render index.html')
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    print('Render play()')
    choices = ['rock', 'paper', 'scissors']
    user_choice = request.json['choice']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })


if __name__ == "__main__":
    app.run(debug=True)
