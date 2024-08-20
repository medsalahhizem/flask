from flask import Flask, render_template
app = Flask(__name__)


@app.route('/Checkerboard')
def level_one():
    return render_template("index.html", num1=8, num2=8, color1="black", color2="white")

@app.route('/Checkerboard/<int:num>')
def level_two(num):
    return render_template("index.html", num1=num, num2=8, color1="black", color2="white")

@app.route('/Checkerboard/<int:num1>/<int:num2>')
def level_three(num1, num2):
    return render_template("index.html", num1=num1, num2=num2, color1="black", color2="white")

@app.route('/Checkerboard/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def level_four(num1, num2, color1, color2):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2=color2)



if __name__ == "__main__":
  app.run(debug=True)