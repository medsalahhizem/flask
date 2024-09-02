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
    print("Creating ninja with data: ", request.form)
    ninja.Ninja.save(request.form)
    return redirect('/')

@app.route('/ninjas/edit/<ninja_id>')
def edit_page(ninja_id):
  print("in edit route for ninja id: ", ninja_id)
  ninja_object=ninja.Ninja.get_one_by_id(ninja_id)
  dojos = dojo.Dojo.get_all()
  return render_template('edit_ninja.html',ninja=ninja_object,all_dojos=dojos)


@app.route('/ninjas/delete/<ninja_id>/<dojo_id>')
def delete_ninja(ninja_id, dojo_id):
  print("Deleting ninja with id:", ninja_id)
  ninja.Ninja.delete_by_id(ninja_id)
  return redirect(f'/dojos/{dojo_id}')



@app.route('/ninjas/update', methods=["POST"])
def update_ninja():
  print("In update to update ninja with data: ", request.form)
  ninja.Ninja.update(request.form)
  return redirect(f'/dojos/{request.form["dojo_id"]}')
