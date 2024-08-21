from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = int(request.form.get('strawberry', 0))
    raspberry = int(request.form.get('raspberry', 0))
    apple = int(request.form.get('apple', 0))
    first_name = request.form.get('first_name', 'Unknown')
    last_name = request.form.get('last_name', 'Unknown')
    student_id = request.form.get('student_id', 'Unknown')

    total_items = strawberry + raspberry + apple

    return render_template("checkout.html", 
                          strawberry=strawberry, 
                          raspberry=raspberry, 
                          apple=apple,
                          first_name=first_name,
                          last_name=last_name,
                          student_id=student_id,
                          total_items=total_items)


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
    
    