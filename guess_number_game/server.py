from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Initialize session variables if they are not set
    if 'num' not in session:
        import random
        session['num'] = random.randint(1, 100)
        session['attempts'] = 0
        session['guess'] = None
        session['error'] = None

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        user_guess = int(request.form['guess'])
    except ValueError:
        # Set an error message in the session if the input is not a number
        session['error'] = 'Please enter a valid integer.'
        return redirect(url_for('index'))
    
    # Update the session with the guess and attempt count
    session['guess'] = user_guess
    session['attempts'] = session.get('attempts', 0) + 1

    # Only update game status if guess is not None
    if session.get('guess') is not None:
        if user_guess == session['num']:
            session['error'] = None
            return redirect(url_for('index'))
        elif session['attempts'] >= 5:
            session['error'] = None
            return redirect(url_for('index'))
    
    return redirect(url_for('index'))
  
@app.route('/reset')
def reset():
    session.pop('num', None)
    session.pop('attempts', None)
    session.pop('guess', None)
    session.pop('error', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
