from flask import render_template, request, redirect
from dojo_ninja_crud import app
from dojo_ninja_crud.models.dojo import Dojo

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos=dojos)

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=dojos)

@app.route('/dojos', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data={"id":id}
    return render_template("show_dojo.html", dojo=Dojo.get_one_with_ninjas(data))
