# flask_app/controllers/dojos.py

from flask import render_template, request, redirect
from dojo_ninja_crud import app
from dojo_ninja_crud.models.dojo import Dojo
from dojo_ninja_crud.models.ninja import Ninja

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojo.html", all_dojos=dojos)

@app.route('/dojos', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    dojo = Dojo.get_by_id(dojo_id)
    ninjas = Ninja.get_by_dojo(dojo_id)
    return render_template("show_dojo.html", dojo=dojo, ninjas=ninjas)
