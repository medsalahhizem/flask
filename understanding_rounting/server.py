from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
      

@app.route('/dojo')
def dojo():
    return "dojo!"



@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    if name.isalpha():  # Ensure the name contains only alphabetic characters
      return "Hi " + name + "!"
    else:
        return "Invalid name. Please enter a valid string."
  
  
  




@app.route('/repeat/<name>/<int:num>')
def show_user_profile(num, name):
    if isinstance(num, int) and name.isalpha():  # Ensure num is an integer and name is a string
        repeated_name = name * num
        return repeated_name
    else:
        return "Invalid input. Please provide a valid string and integer."

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

