from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from app import db 
from models import User, Visit, City 

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def users():
    cities = City.query.all()
    return render_template("cities/index.jinja", cities=cities)



