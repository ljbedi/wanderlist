from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from app import db 
from models import User, Visit, City 

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def users():
    cities = City.query.all()
    return render_template("cities/index.jinja", cities=cities)


# @cities_blueprint.route("/cities/show/<id>")
# def show(id):
#     city = City.query.get(id)
#     users = User.query.join(Visit).filter(Visit.city_id == id)
#     return render_template("cities/show.jinja", city=city, users=users)

@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("cities/new.jinja")

@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    city = request.form['city']
    country = request.form['country']
    city = City(name=city, country=country)
    db.session.add(city)
    db.session.commit()
    return redirect('/cities')

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    City.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/cities')

@cities_blueprint.route("/cities/<id>")
def city_info(id):
    city = City.query.get(id)
    return render_template("cities/show.jinja", city=city)


