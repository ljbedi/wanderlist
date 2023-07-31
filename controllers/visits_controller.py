from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from app import db 
from models import User, Visit, City 

visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def visits():
    visits = Visit.query.all()
    return render_template("visits/index.jinja", visits=visits)

@visits_blueprint.route("/visits/new", methods=['GET'])
def new_visit():
    users = User.query.all()
    cities = City.query.all()
    return render_template("visits/new.jinja", users = users, cities=cities)

@visits_blueprint.route("/visits",  methods=['POST'])
def create_visit():
    user_id = request.form['user_id']
    city_id = request.form['city_id']
    visit = Visit(user_id = user_id, city_id = city_id)
    db.session.add(visit)
    db.session.commit()
    return redirect('/visits')