import datetime

from app import db

# Example Model
# ------------------------------------------------
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))

# What are we doing here? We are defining our models that we will give to the database and then can be called upon on
# program. We define what the column will be and then we tell them what value this property will have. 
# The def __repr__ is there to make sure we represent our objects with names rather than <03992>? 

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    date_joined = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    visits = db.relationship('Visit', backref='user')

    def __repr__(self):
        return f"User: {self.id}: {self.name}"

class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)
    visited = db.Column(db.Boolean, server_default="false")
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id", ondelete = "CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete = "CASCADE"))

    def __repr__(self):
        return f"Visit {self.id}: {self.visited}"


class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    country = db.Column(db.String(70))
    visits = db.relationship('Visit', backref ='city')
    
    def __repr__(self):
        return f"City {self.id}: {self.name}"

