#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/19 16:52
@Desc   ：
=================================================='''
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo_id1': {'task': '这是任务1'},
    'todo_id2': {'task': '这是任务2'},
    'todo_id3': {'task': '这是任务3'}
}

parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, todo_id):
        return TODOS[todo_id]

    def delete(self, todo_id):
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return TODOS


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == "__main__":
    app.run(debug=True)
