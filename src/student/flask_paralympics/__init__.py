import os
from flask import Flask

def create_app(test_config=None):
    '''Create and configure an instance of the Flask application'''
   
    # Create the Flask app
    app = Flask(__name__, instance_relative_config=True)
    
    # Configure the Flask app
    app.config.from_mapping(
        SECRET_KEY = '5U3qTxfvPSuMfxv3ZztdCQ',
        # Set the location of the database file called paralympics.sqlite
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.instance_path, 'paralympics.sqlite'), # change instance to flask instance database
    )
        
    if test_config is None:        
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)    
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)
        
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        
    except OSError:
        pass
    
    with app.app_context():
        
        # Register the blueprint
        from .routes import main

        app.register_blueprint(main)
        
    return app