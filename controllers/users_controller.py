from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from models import User, Visit, City
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)

