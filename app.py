from urllib import response
from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from permissions import Permissions

app = Flask(__name__)
api = Api(app)


class Task:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }


tasks = [
    Task(1, "Buy new pencil"),
    Task(2, "Go run"),
    Task(3, "Take your dog out")
]

class TodoListCreate(Resource):
    parser = RequestParser(bundle_errors=True)
    parser.add_argument("task", required=True, type=str)
    
    def get(self):
        response = []
        for el in tasks: response.append(el.json())
        return response, 200
    
    def post(self):
        args = self.parser.parse_args()
        
        if len(tasks) > 0: new_task = Task(tasks[-1].id + 1, args["task"])
        else: new_task = Task(1, args["task"])
        
        tasks.append(new_task)
        return new_task.json(), 201
    
    
api.add_resource(TodoListCreate, "/todos/")

if __name__ == '__main__':
    app.run(port=5000, debug=True)