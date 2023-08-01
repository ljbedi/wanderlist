from flask import Flask, render_template, redirect, request 
from flask import Blueprint 
from models import User, Visit, City
from app import db

users_blueprint = Blueprint("users", __name__)

# @users_blueprint.route("/users")
# def users():
#     users = User.query.all()
#     return render_template("users/index.jinja", users=users)

# @users_blueprint.route("/users/new", methods=['GET'])
# def new_user():
#     users = User.query.all()
#     cities = City.query.all()
#     return render_template("users/new.jinja", users=users, cities=cities)

# @users_blueprint.route("/users")
# def create_user():
#     return render_template("users/new.jinja")

# @users_blueprint.route("/users",  methods=['POST'])
# def create_new_user():
#     name = request.form['name']
#     user = User(name=name)
#     db.session.add(user)
#     db.session.commit()
#     return redirect('/users')

@users_blueprint.route("/users/<id>")
def show(id):
    user = User.query.get(id)
    cities = City.query.join(Visit).filter(Visit.user_id == id)
    return render_template("users/show.jinja", user=user, cities=cities)

# @users_blueprint.route("/users/<id>/delete", methods=['POST'])
# def delete_user(id):
#     User.query.filter_by(id = id).delete()
#     db.session.commit()
#     return redirect('/users')

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)

@users_blueprint.route("/users/new", methods=['GET'])
def new_user():
    users = User.query.all()
    cities = City.query.all()
    return render_template("users/new.jinja", users = users, cities=cities)

@users_blueprint.route("/users",  methods=['POST'])
def create_user():
    name = request.form['name']
    user = User(name = name)
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@users_blueprint.route("/users/<id>/delete", methods=['POST'])
def delete_user(id):
    User.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect(f'/users')

@users_blueprint.route("/users/<id>/add", methods=['POST'])
def add_visit_to_user(id):
    pass

