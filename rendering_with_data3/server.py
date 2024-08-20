from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def render_lists():
    student_info = [
      {'name' : 'Michael', 'last_name':'Jackson'},
      {'name' : 'Salah', 'last_name' :'Hizem'},
      {'name' : 'Hamza', 'last_name' :'Aloui'},
      {'name' : 'Sami', 'last_name' :'Hethli'},
    ]
    return render_template("index.html", students = student_info)
  
if __name__ == "__main__":
  app.run(debug=True)