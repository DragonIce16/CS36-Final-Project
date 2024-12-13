from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Game state
game_state = {
    'target_number': None,
    'accuracy_required': None,
    'guess_count': 0,
    'feedback_messages': [],
    'game_over': False
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'reset' in request.form:
            # Reset game
            game_state['target_number'] = None
            game_state['accuracy_required'] = None
            game_state['guess_count'] = 0
            game_state['feedback_messages'] = []
            game_state['game_over'] = False
        
        elif 'generate' in request.form:
            # Start game with inputed number
            user_number = request.form.get('number')
            game_state['target_number'] = int(user_number) if user_number else None
            game_state['accuracy_required'] = float(request.form.get('accuracy', 10))
            game_state['guess_count'] = 0
            game_state['feedback_messages'] = []
            game_state['game_over'] = False

        elif 'random' in request.form:
            # Generate random number
            game_state['target_number'] = random.randint(50, 250)
            game_state['accuracy_required'] = 10  # Default
            game_state['guess_count'] = 0
            game_state['feedback_messages'] = []
            game_state['game_over'] = False

        elif 'guess' in request.form:
            if game_state['target_number'] is None:
                game_state['feedback_messages'].append("Please set a target number first!")
                return render_template('game.html', game_state=game_state)
                
            guess = float(request.form.get('user_guess', 0))
            game_state['guess_count'] += 1
    
            actual_sqrt = (game_state['target_number'] ** 0.5)
            percentage_diff = abs(guess - actual_sqrt) / actual_sqrt * 100
            
            if percentage_diff <= game_state['accuracy_required']:
                game_state['feedback_messages'].append(f"Correct! You got it in {game_state['guess_count']} tries!")
                game_state['game_over'] = True
            else:
                if guess < actual_sqrt:
                    game_state['feedback_messages'].append("Too low, try again!")
                else:
                    game_state['feedback_messages'].append("Too high, try again!")
    
    return render_template('game.html', game_state=game_state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')