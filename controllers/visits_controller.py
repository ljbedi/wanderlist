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
    args = request.args
    user_id = args.get("user")
    if user_id:
        user_id = int(user_id)
    return render_template("visits/new.jinja", users = users, cities=cities, user_id=user_id)

@visits_blueprint.route("/visits",  methods=['POST'])
def create_visit():
    user_id = request.form['user_id']
    city_id = request.form['city_id']
    visited = "visited" in request.form
    visit = Visit(user_id = user_id, city_id = city_id, visited=visited)
    db.session.add(visit)
    db.session.commit()
    return redirect(f'/users/{user_id}')

@visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
def delete_visit(id):
    Visit.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect(f'/visits')

@visits_blueprint.route("/users/<user_id>/visits/<visit_id>/delete", methods=['POST'])
def user_delete_visit(user_id, visit_id):
    Visit.query.filter_by(id = visit_id).delete()
    db.session.commit()
    return redirect(f'/users/{user_id}')

@visits_blueprint.route("/users/<user_id>/visits/<visit_id>/visited", methods =['POST'])
def visited(user_id, visit_id):
    visit = Visit.query.get(visit_id)
    visit.visited = True
    db.session.commit()
    return redirect(f'/users/{user_id}')


