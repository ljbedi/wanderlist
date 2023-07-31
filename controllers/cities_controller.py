from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from app import db 
from models import User, Visit, City 

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def users():
    cities = City.query.all()
    return render_template("cities/index.jinja", cities=cities)

@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    user_id = request.form['user_id']
    city_id = request.form['city_id']
    visit = Visit(user_id = user_id, city_id = city_id)
    db.session.add(visit)
    db.session.commit()
    return redirect('/cities')

@cities_blueprint.route("/cities/show/<id>")
def show(id):
    city = City.query.get(id)
    users = User.query.join(Visit).filter(Visit.city_id == id)
    return render_template("cities/show.jinja", city=city, users=users)

@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("cities/new.jinja")

