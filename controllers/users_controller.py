from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from models import User, Visit, City
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)

@users_blueprint.route("/users/<id>")
def show(id):
    user = User.query.get(id)
    cities = City.query.join(Visit).filter(Visit.user_id == id)
    return render_template("users/show.jinja", user=user, cities=cities)

@users_blueprint.route("/users",  methods=['POST'])
def create_user():
    return render_template("users/new.jinja")

