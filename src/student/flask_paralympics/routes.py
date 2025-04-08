from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# the route function and the route definitions
@main.route('/')
def index():
    return render_template('index.html')

