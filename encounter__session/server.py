from flask import Flask, render_template, session, redirect
app=Flask(__name__)
app.secret_key="secret_key"
@app.route('/')
def index():
  if "count" not in session:
    session ["count"] = 0
  else: 
    session ["count"] += 1
  return render_template("index.html")

@app.route('/increment')
def increment():
  return redirect('/')

@app.route('/incrementby2')
def incrementby2():
  session['count'] +=1
  return redirect('/')

@app.route('/reset')
def reset():
  session.pop("count") # Reset specific session data
  return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear() 
    # Clear all session data
    return redirect('/')


if __name__ == "__main__":
  app.run(debug=True)