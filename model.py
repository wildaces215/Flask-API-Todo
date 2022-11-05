from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from dataclasses import dataclass
db = SQLAlchemy()

@dataclass
class Todo(db.Model):
    id:int
    task:str
    description:str
    id = db.Column(db.Integer,primary_key = True)
    task = db.Column(db.String(100))
    description = db.Column(db.String(100))