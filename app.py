from flask import Flask , request,Response,jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from model import db,Todo
from sqlalchemy_serializer import SerializerMixin


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
@app.before_first_request
def table_creation():
    db.create_all()
@app.route('/')
def home():
    todo_res = Todo.query.all()
    return jsonify(todo_res)
   
@app.route('/new',methods=["POST"])
def new():
    req_data = request.get_json()
    new_todo = Todo(task=req_data['task'],description=req_data['description'])
    db.session.add(new_todo)
    db.session.commit()
    return "Created new todo"

@app.route('/update',methods=['POST'])
def update():
    data = request.get_json()
    todo = Todo.query.filter_by(id=data[id]).first()
    todo.task = data['task']
    todo.description = data['description']
    db.session.commit()
    return 'Updated todo'

@app.route('/delete',methods=['POST'])
def delete():
    del_qry_id = request.get_json()
    del_qry = Todo.query.filer_by(id=del_qry_id['id']).first()
    db.session.delete(del_qry)
    return 'Deleted query'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)