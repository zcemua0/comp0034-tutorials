# " This is the blueprint method Flask"

# Import the Flask class from the Flask library
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# the route function and the route definitions
@main.route('/')
def index():
    return f"Welcome to the Paralympics app!"
