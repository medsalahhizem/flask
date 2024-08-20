from flask import Flask,render_template  # Import Flask to allow us to create our app

app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<string:color>')
def play(x=3, color='blue'):
    return render_template('index.html', count=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)



