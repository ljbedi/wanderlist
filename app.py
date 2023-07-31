from flask import Flask, render_template, redirect, request 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# Here we are importing necessary modules for building the Flask app and interacting with the database. 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://liambailey@localhost:5432/bucketlist_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Here we are initializing our Flask app and telling it where to find it. 

from models import User, Visit, City

# Here we are importing our models, these are our database tables and where we highlight which models have 
# relationships with others. 

@app.route("/")
def homepage():
    return render_template("index.jinja", title="Wanderlist")

# Here we are just defining our route homepage and what we want that to show when we type in that link. 

from controllers.visits_controller import visits_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.users_controller import users_blueprint

app.register_blueprint(visits_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(users_blueprint)

# ??? I'm not sure what the blueprint is doing??? Ensuring it does what we have told it to do? 