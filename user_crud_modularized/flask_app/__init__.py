from flask import Flask
app = Flask(__name__)

# Import the controllers
from flask_app.controllers import users
