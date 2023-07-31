from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from app import db 
from models import User, Visit, City 

visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def visits():
    visits = Visit.query.all()
    return render_template("visits/index.jinja", visits=visits)

