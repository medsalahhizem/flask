# flask_app/controllers/ninjas.py

from flask import render_template, request, redirect
from dojo_ninja_crud import app
from dojo_ninja_crud.models.ninja import Ninja
from dojo_ninja_crud.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninja.html", all_dojos=dojos)

@app.route('/ninjas', methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect(f'/dojos/{request.form["dojo_id"]}')
