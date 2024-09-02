from flask import Flask, render_template
from BURGERS.models.burger import Burger
from BURGERS.models.topping import Topping

app = Flask(__name__)

@app.route('/')
def index():
    print("Index route accessed")  # Debug print
    burgers = Burger.get_all()
    toppings = Topping.get_all()
    return render_template('index.html', burgers=burgers, toppings=toppings)

@app.route('/burger/<int:id>')
def show_burger(id):
    data = {'id': id}
    print(f"Burger route accessed with id: {id}")  # Debug print
    burger = Burger.get_burger_with_toppings(data)
    return render_template('burger_with_toppings.html', burger=burger)

@app.route('/topping/<int:id>')
def show_topping(id):
    data = {'id': id}
    print(f"Topping route accessed with id: {id}")  # Debug print
    topping = Topping.get_topping_with_burgers(data)
    return render_template('topping_with_burgers.html', topping=topping)

if __name__ == '__main__':
    app.run(debug=True)
