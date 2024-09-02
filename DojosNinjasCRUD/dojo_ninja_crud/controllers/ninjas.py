from flask import render_template, request, redirect
from dojo_ninja_crud import app
from dojo_ninja_crud.models import ninja,dojo

@app.route('/ninjas')
def ninjas():
    dojos = dojo.Dojo.get_all()
    return render_template("ninja.html", all_dojos=dojos)
  
@app.route('/home')
def home():
    return render_template("index.html",)

@app.route('/ninjas', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
