from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship



db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    computation = relationship("Computation")

    def __repr__(self):
        return '<User %r>' % self.username


class Computation(db.Model):
    __tablename__ = "computation"

    id = db.Column(db.Integer, primary_key=True)
    number_of_unknowns = db.Column(db.Integer)
    left_bound = db.Column(db.Integer)
    right_bound = db.Column(db.Integer)
    computation_time = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f'<Computation  {self.id}\tCount  {self.number_of_unknowns}\tTime  {self.computation_time}> '